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
