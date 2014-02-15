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
  srcArray = s;
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
