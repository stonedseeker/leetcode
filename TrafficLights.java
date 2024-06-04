class TrafficLights {
  String color;
  float duration;

  TrafficLights (String color, float duration) {
    this.color = color;
    this.duration = duration;
  }

  public void toggle() {
    if (this.color == "RED") {
      this.color = "GREEN";
    } else {
      this.color = "RED";
    }
  }

  public void get_details() {
    System.out.println(this.color + " " + this.duration);
  }

  public static void main(String[] args) {
    TrafficLights khmba = new TrafficLights("RED", 25);
    khmba.get_details();

    khmba.toggle();
    khmba.get_details();
 }

}
