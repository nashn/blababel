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
