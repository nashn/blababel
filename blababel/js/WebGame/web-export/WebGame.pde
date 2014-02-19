static int GAME_SCORE = 0;
static boolean gameOver;
static boolean gamePaused;
static boolean gameStart;
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
Boolean stopMovingX = false;
interface JavaScript {
  void getScore(int i);
  void getEndGameResult(bool b);
  void setSourceStringArray(String[] s);
  void setDestStringArray(String[] s);
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

void setSourceStringArray(String[] s)
{
  srcArray = s;
}

void setDestStringArray(String[] s)
{
  destArray = s;
}

void randomizeArrays(String[] a, String[] b)
{
  for (int i=0; i < a.length; ++i) {
    int bool = Math.floor((Math.random()*2)+1);
    if (bool == 1) {
      int rand = Math.floor((Math.random()*a.length));
      console.log(rand);
      String temp = a[rand];
      a[rand] = b[rand];
      b[rand] = temp;
    }
  }
}

void setup()
{
  size(320, 480);
  //gamePaused = true;
  //gameOver = false;
  buttonList = new ArrayList<Button>();
  currentButton = new Button(srcArray[0], destArray[0], "c");
  buttonList.add(currentButton);
  currentButton.setCurrent();
  nextButton = new Button(srcArray[1], destArray[1], "c");
  buttonList.add(nextButton);
  startTime = millis();
  startPage();
}
void startPage()
{
  gameStart = true;
  gamePaused = true;
  textSize(30);
  textAlign(CENTER);
  text("   Try to match the", width/2, height/2);
  text("  translations by using", width/2, height/2+50);
  text("  <> or LEFT RIGHT", width/2, height/2 +100);
  fill(0,0,0,150);
  rect(0,0,width,height);
  
}
void restart()
{
  randomizeArrays(srcArray, destArray);
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
  strokeWeight(10);
  stroke(128,128,128);
  fill(204,229,255);
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
  if (GAME_SCORE == 5) {
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
  if(gameStart)
  {
    gameStart = false;
    gamePaused = false;
    randomizeArrays(srcArray, destArray);
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
  static int n = 1;
  int px, py, boxWidth, boxHeight;
  color boxColor;
  color textColor;
  static boolean stopMovingX = false;
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
    
    switch(n)
    {
      
      case 1:
            boxColor = color(255,213,0);
            break;
      case 2:
            boxColor = color(249,100,100);
            break;
      case 3:
            boxColor = color(0 ,153,0);
            break;
      case 4:
            boxColor = color(219,100,249);
            break;
      case 5: 
            boxColor = color(0,0,102);
            break;
      
    }
    if(n <=4)
      n++;
     else
      n=1;
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
  /* if(this.px + boxWidth + 1 <= o.px && (this.py > o.py + boxHeight && this.py < op.y + boxHeight))
    {
      stopMovingX = true;
      return true;
    }*/
      stopMovingX = false;
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
    py = py + 3;
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
    
    if (temp < 0 || temp >= width || stopMovingX) {
      return;
    }
    px += num;
  }
  
  public void display()
  {
    if (!active)
      return;
    
    fill(boxColor);
    strokeWeight(1);
    smooth();
    stroke(0,0,0);
    rect(px, py, boxWidth, boxHeight, 10);
    
    textSize(20);
    textAlign(CENTER);
    fill(textColor);
    text(srcLang, px, py+10, boxWidth, boxHeight);
  }
}

