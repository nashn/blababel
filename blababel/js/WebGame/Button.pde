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
    textAlign(CENTER);
   
    fill(255,255,255);
    text(srcLang, x + COLUMN_2X, y + BOX_HEIGHT + 5, BOX_WIDTH, BOX_HEIGHT/2);
  }
  
  public void display(Button b)
  {
    fill(0, 0, 0);
    rect(390,70, 90, 40);
    
    textSize(12);
    textAlign(CENTER);
   
    fill(255,255,255);
    text(b.srcLang, 390, 80, 90, 40);
  }
 
}
