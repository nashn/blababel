static int GAME_SCORE = 0;
static boolean gameOver;
static boolean gamePaused;

static float startTime;
static float currentTime;
ArrayList<Button> buttonList;
String[] srcArray = {"boy", "cboy", "girl", "apple", "capple","man", "woman", "cman"};
String[] destArray = {"cboy", "boy", "cgirl", "capple", "apple","cman", "cwoman", "man"};
int nextWordIndex;

Button currentButton;
Button nextButton;
int currentButtonIndex;
Boolean currentButtonIsFinished = true;

interface JavaScript {
  void getScore(int i);
  void getEndGameResult(bool b);
  void pause();
  void restart();
  void btnLeft();
  void btnRight();
}

void btnLeft() { currentButton.moveX(-80); } 
void btnRight() { currentButton.moveX(80); }
void pause() { gamePaused = !gamePaused; }
void bindJavascript(JavaScript js) { javascript = js; }
JavaScript javascript;

void scoreIncrease()
{
  if(javascript != null) {
    javascript.getScore(GAME_SCORE);
  }
}

void setup()
{
  size(320, 480);
  gamePaused = false;
  gameOver = false;
  buttonList = new ArrayList<Button>();
  currentButton = new Button(srcArray[0], destArray[0], "c");
  buttonList.add(currentButton);
  currentButton.setCurrent();
  nextButton = new Button(srcArray[1], destArray[1], "c");
  buttonList.add(nextButton);
  startTime = millis();
}

void restart()
{
  gamePaused = false;
  gameOver = false;
  GAME_SCORE = 0;
  buttonList = new ArrayList<Button>();
  currentButton = new Button(srcArray[0], destArray[0], "c");
  buttonList.add(currentButton);
  currentButton.setCurrent();
  nextButton = new Button(srcArray[1], destArray[1], "c");
  buttonList.add(nextButton);
  startTime = millis();
}

void base()
{
  // Clear background
  fill(255,255,255);
  rect(0,0,width,height);
  
  // Draw arrows
  fill(0,0,0);
  triangle(0,height/2,10,height/2-5,10,height/2+5);
  triangle(width,height/2,width-10,height/2-5,width-10,height/2+5);
}

void draw()
{
  if (gamePaused) {
    return;
  }
  if (GAME_SCORE == 3) {
    winGame();
    return;
  }
  if (gameOver) {
    endGame();
    return;
  }
  
  base();
  
  if (currentButtonIsFinished) {
    if (nextWordIndex > srcArray.length-1) {
      nextWordIndex = 0;
    }
    currentButton = nextButton;
    currentButton.setCurrent();
    nextButton = new Button(srcArray[nextWordIndex], destArray[nextWordIndex++], "c");
    buttonList.add(nextButton);
    currentButtonIsFinished = false;
  }
  currentButton.move();
  
  buttonLoop: for (int i=0; i < buttonList.size(); ++i) {
    Button tempButton = buttonList.get(i);
    if (!tempButton.active) {
      buttonList.remove(i);
      continue buttonLoop;
    }
    tempButton.display();
    
    if (buttonList.get(i) != currentButton) {
      if (buttonList.get(i).isColliding(currentButton)) {
        currentButtonIsFinished = true;
      }
    }
  }
  
  currentTime = millis() - startTime;
}

void keyPressed()
{  
  switch(keyCode) {
    case DOWN : currentButton.moveY(5);
      break;
    case LEFT : currentButton.moveX(-80);
      break;
    case RIGHT : currentButton.moveX(80);
      break;
  }
}

void mouseClicked()
{
  if (mouseX < width/2) {
    currentButton.moveX(-80);
  } else {
    currentButton.moveX(80);
  }
}

public void winGame()
{
  fill(0,0,0,150);
  rect(0,0,width,height);
  gamePaused = true;
  textSize(45);
  textAlign(CENTER);
  text("CONGRATS", width/2, height/2);
  if(javascript != null) {
    javascript.getScore(GAME_SCORE);
    javascript.getEndGameResutl(true);
  }
}

public void endGame()
{
  fill(0,0,0,150);
  rect(0,0,width,height);
  gamePaused = true;
  textSize(45);
  textAlign(CENTER);
  text("GAME OVER", width/2, height/2);
  if(javascript != null) {
    javascript.getEndGameResult(false);
  }
}
class Button
{ 
  String srcLang;
  String destLang;
  String spelling;
  boolean active;
  
  int px, py, boxWidth, boxHeight;
  color boxColor;
  color textColor;
  
  public Button(String srcLang, String tranLang, String spelling)
  {
    this.srcLang = srcLang;
    this.destLang = tranLang;
    this.spelling = spelling;
    currentButtonIsFinished = false;
    this.active = true;
    px = -100;
    py = -100;
    boxWidth = 79;
    boxHeight = 48;
    boxColor = color(0,0,0);
    textColor = color(255,255,255);
  }
  
  public void setCurrent()
  {
    px = 80;
    py = -20;
  }
  
  public boolean isColliding(Button o)
  {
    if (!(this.px > o.px+o.boxWidth || this.px+this.boxWidth < o.px 
      || this.py > o.py+o.boxHeight || this.py+this.boxHeight < o.py)) {
      if ((this.srcLang.equals(o.destLang)) && (this.py > o.py)) {
        this.active = false;
        o.active = false;
        GAME_SCORE++;
        scoreIncrease();
      }
      if (this.py <= 10) {
        gameOver = true;
      }
      return true;
    }
    return false;
  }
  
  public void move()
  {
    if(py >= height-boxHeight) {
      currentButtonIsFinished = true;
      return;
    }
    py = py + 5;
  }
  
  public void moveY(int num)
  {
    if(py >= height-boxHeight) {
      currentButtonIsFinished = true;
      return;
    }
    py = this.py + 1;
  }
  
  public void moveX(int num)
  {
    int temp = px + num;
    if (temp < 0 || temp >= width) {
      return;
    }
    px += num;
  }
  
  public void display()
  {
    if (!active)
      return;
    
    fill(boxColor);
    noStroke();
    rect(px, py, boxWidth, boxHeight);
    
    textSize(12);
    textAlign(CENTER);
    fill(textColor);
    text(srcLang, px, py+10, boxWidth, boxHeight);
  }
}

