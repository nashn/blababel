String Lesson = "Lesson: 1";
String Step = "Score: ";
String Time = "Time: ";
Boolean currentButtonIsFinished = true;
int count = 0;

static final int CANVAS_WIDTH = 575;
static final int CANVAS_HEIGHT = 500;
static final int GAME_WIDTH = 276;
static final int GAME_HEIGHT = 440;
static int GAME_SCORE = 0;
static boolean gameOver = false;
static boolean gamePaused = false;
static boolean justOutOfgamePaused = false;

static float startTime;
static float pausedTime;
static float currentTime;
static float pausedDiff;
static final int BUTTON_TOTAL = 40;
ArrayList<Button> buttonList;
String[] srcArray = {"boy", "cboy", "girl", "apple", "capple","man", "woman", "cman"};
String[] destArray = {"cboy", "boy", "cgirl", "capple", "apple","cman", "cwoman", "man"};
Button currentButton;
Button nextButton;
int currentButtonIndex;
int nextButtonIndex;

void base()
{
  size(CANVAS_WIDTH, CANVAS_HEIGHT);
  //background
  smooth();
  strokeWeight(12);
  stroke(160,160,160,200);
  //fill(139,209,255);
  fill(191,215,232);
  rect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
  //big rect
  smooth();
  strokeWeight(8);
  stroke(102,153,255,200);
  fill(126,187,228);
  rect(25,25, GAME_WIDTH, GAME_HEIGHT);
  //small rect
  smooth();
  strokeWeight(8);
  stroke(102,153,255,200);
  fill(126,187,228);
  rect(325,25, 225, 130);
  //Static Strings
 // textFont(createFont("KacstTitleL", 20));
  textSize(30);
  fill(255,255,255);
  textAlign(LEFT);
  text(Lesson, 325, 200);
  //Restart
  fill(255,255,255);
  rect(325, 340, 80, 40);
  fill(0,0,0);
  textSize(16);
  textAlign(CENTER);
  text("Restart", 325, 350, 80, 40);
  //pause
  fill(255,255,255);
  rect(455, 340, 80, 40);
  fill(0,0,0);
  textSize(16);
  textAlign(CENTER);
  text("Pause", 455, 350, 80, 40);
}

void setup()
{
  gamePaused = false;
  gameOver = false;
  base();
  buttonList = new ArrayList<Button>();
  currentButton = new Button(srcArray[0], destArray[0], "c");
  buttonList.add(currentButton);
  currentButton.setCurrent();
  nextButton = new Button(srcArray[1], destArray[1], "c");
  buttonList.add(nextButton);
  startTime = millis();
}

void draw()
{
 if (gamePaused) {
  return;
 }
 
  if (gameOver) {
    endGame();
    return;
  }
  
  if (currentButtonIsFinished) {
    if (nextButtonIndex > srcArray.length-1) {
      nextButtonIndex = 0;
    }
    currentButton = nextButton;
    currentButton.setCurrent();
    nextButton = new Button(srcArray[nextButtonIndex], destArray[nextButtonIndex++], "c");
    buttonList.add(nextButton);
    currentButtonIsFinished = false;
  }
  currentButton.move();
  
  base();
  nextButton.display(nextButton);
  buttonLoop: for (int i=0; i < buttonList.size(); ++i) {
    Button tempButton = buttonList.get(i);
    if (!tempButton.active) {
      buttonList.remove(i);
      continue buttonLoop;
    }
    //currentButton.display();
    tempButton.display();
    
    if (buttonList.get(i) != currentButton) {
      if (buttonList.get(i).isColliding(currentButton)) {
        currentButtonIsFinished = true;
      }
    }
  }
  
  textSize(30);
  textAlign(LEFT);
  text(Step + GAME_SCORE, 325, 240);
  
  textSize(30);
  textAlign(LEFT);
  if(justOutOfgamePaused)
  {
     text(Time + Float.toString(pausedTime/1000), 325, 280); 
     justOutOfgamePaused = false;
     pausedDiff = millis() - pausedTime;
  }
  else
  {
     currentTime = millis() - startTime;
    text(Time + Float.toString(currentTime/1000), 325, 280);
  }
}

void keyPressed()
{
  if(key == CODED)
  {
    if(keyCode == DOWN)
      currentButton.move(5);
    else if(keyCode == LEFT)
      currentButton.moveX(-69);
    else if(keyCode == RIGHT)
      currentButton.moveX(69);    
  }
}

void mouseClicked()
{
  if((mouseX >= 325 && mouseX <=380)&& (mouseY >=340 && mouseY <=380))
  {
    System.out.println("RESTART!");
    GAME_SCORE = 0;
    setup();
  }
  if(!gameOver){
  if((mouseX >= 455 && mouseX <=535)&& (mouseY >=340 && mouseY <=380))
  {
    gamePaused = !gamePaused;
    justOutOfgamePaused = true;
    pausedTime = millis();
  }
  }
}

public void endGame()
{
  fill(0,0,0,150);
  rect(25,25,GAME_WIDTH,GAME_HEIGHT);
  gamePaused = true;
  textSize(45);
  textAlign(CENTER);
  text("GAME OVER", GAME_WIDTH/2 + 25, GAME_HEIGHT/2);
}
/*
**This class creates a button object
**A button object contains the vocab and its translation
*/
class Button
{
  static final int COLUMN_2X = 94;
  static final int BOX_WIDTH = 69;
  static final int BOX_HEIGHT = 44;
  static final int BOUNDARY_LEFT = 25;
  static final int BOUNDARY_RIGHT = 301;
  static final int BOUNDARY_TOP = 25;
  
  private String srcLang;
  private String destLang;
  private String spelling;
  private float y = 0;
  private float x = 0;
  private boolean active;
  
  public Button(String srcLang, String tranLang, String spelling)
  {
    this.srcLang = srcLang;
    this.destLang = tranLang;
    this.spelling = spelling;
    currentButtonIsFinished = false;
    this.active = true;
    x = -100;
    y = -100;
  }
  public Button()
  {
    rect(400,70, 70, 30);
  }
  
  public void setCurrent()
  {
    x = 0;
    y = -20;
    //rect(COLUMN_2X, 40, BOX_WIDTH, BOX_HEIGHT);
  }
  
  public float currentX()
  {
    return COLUMN_2X + x;
  }
  public float currentY()
  {
    return BOX_HEIGHT + y;
  }
  public String getSrc()
  {
    return srcLang;
  }
  public String getTran()
  {
    return destLang;
  }
  public String getSpell()
  {
    return spelling;
  }
  
  public boolean isColliding(Button b) 
  {
   if ((this.currentY() <= b.currentY()+BOX_HEIGHT-5) && (this.currentX() == b.currentX())) {
     if (this.srcLang.equals(b.destLang)) {
       this.active = false;
       b.active = false;
       GAME_SCORE++;
     }
     if (b.currentY() <= BOUNDARY_TOP+10) {
       gameOver = true;
     }
     return true;
   }
   return false;
  }
  
  public void move()
  {
    if(y >= 387)
    {
      currentButtonIsFinished = true;
       return;
    }
      y = y + 10;
  }
  public void move(int num)
    {
    if(y >= 387)
    {
      currentButtonIsFinished = true;
       return;
    }
      y = y + 1;
    }
  public void moveX(int num)
  {
    if (this.currentX()+num <= BOUNDARY_LEFT) {
      x = -62;
      return;
    }
    if (this.currentX()+num+BOX_WIDTH-1 >= BOUNDARY_RIGHT) {
      x = 2 * BOX_WIDTH - 2;
      return;
    }
    x += num;
  }
  public void display()
  {
    if (!active)
      return;
    
    fill(0,0,0);
    rect(x + COLUMN_2X, y + BOX_HEIGHT, 70, 30);
    textSize(12);
    textAlign(CENTER, CENTER);
   
    fill(255,255,255);
    text(srcLang, x + COLUMN_2X, y + BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT/2);
  }
  
  public void display(Button b)
  {
    fill(0, 0, 0);
    rect(390,70, 90, 40);
    textSize(12);
    textAlign(CENTER, CENTER);
   
    fill(255,255,255);
    text(b.srcLang, 390, 70, 90, 40);
  }
 
}

