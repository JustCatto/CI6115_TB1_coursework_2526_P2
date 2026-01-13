package q3;

public class OrderTracking implements Observer {

  private static OrderTracking instance;

  private OrderTracking() {}

  public static OrderTracking getInstance() {
    if (instance == null) {
      instance = new OrderTracking();
    }
    return instance;
  }

  public void update() {
    System.out.println("Adding order to queue and getting postage tracking details...");
  }
}
