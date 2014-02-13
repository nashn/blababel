String Lesson = "Lesson: 1";
String Steps = "Steps:   0";
Button B;
Button A;
Boolean releaseMoreBrick = true;
int count = 0;
void base()
{
   size(575, 500);
  //background
  smooth();
  strokeWeight(12);
  stroke(160,160,160,200);
  //fill(139,209,255);
  fill(191,215,232);
  rect(0,0,575,500);
  //big rect
  smooth();
  strokeWeight(8);
  stroke(102,153,255,200);
  fill(126,187,228);
  rect(25,25, 275, 450);
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
  text(Lesson, 325, 200);
  textSize(30);
  text(Steps, 325, 240);
}

void setup()
{
  base();
  B = new Button("asdf","asdf","asdf");
  A = new Button();
}
void draw()
{
  /*if(releaseMoreBrick)
    B = new Button();*/
  B.move();
  B.display();
}
/*
**This class creates a button object
**A button object contains the vocab and its translation
*/
class Button
{
  private String srcLang;
  private String tranLang;
  private String spelling;
  private float y = 0;
  private float x = 0;
  public Button(String srcLang, String tranLang, String spelling)
  {
    this.srcLang = srcLang;
    this.tranLang = tranLang;
    this.spelling = spelling;
    rect(125, 40, 70, 30);
    releaseMoreBrick = false;
  }
  public Button()
  {
    rect(400,70, 70, 30);
  }
  public float currentX()
  {
    return 125 + x;
  }
  public float currentY()
  {
    return 40 + y;
  }
  public String getSrc()
  {
    return srcLang;
  }
  public String getTran()
  {
    return tranLang;
  }
  public String getSpell()
  {
    return spelling;
  }
  public void move()
  {
    if(y >= 420)
    {
      releaseMoreBrick = true;
       return;
    }
      y = y + 1;
  }
  public void move(int num)
    {
    if(y >= 420)
    {
      releaseMoreBrick = true;
       return;
    }
      y = y + 1;
    }
  public void moveX(int num)
  {
    x += num;
  }
  public void display()
  {
    base();
     rect(125 + x, 25+y, 70, 30);
     rect(390,70, 90, 40);
  }
  
 
}
void frameCollision(Button b)
{
  float frameX = 25 + 275;
  float frameY = 25 + 450;
  float bX = b.currentX() + 70;
  float bY= b.currentY() + 40;
    if(25 < bY  && frameY > bY){
      if (25 < bX && frameX > bX) 
          return;
    }
    if(25 < b.currentY()  && frameY > b.currentY()){
      if (25 < b.currentX() && frameX > b.currentX()) 
          return;
    }

    println("hit %d", count++);
}
void keyPressed()
{
  frameCollision(B);
  if(key == CODED)
  {
    if(keyCode == DOWN)
      B.move(5);
    else if(keyCode == LEFT)
      B.moveX(-5);
    else if(keyCode == RIGHT)
      B.moveX(5);    
  }
}

