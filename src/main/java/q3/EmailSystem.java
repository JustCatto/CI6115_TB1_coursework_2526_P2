package q3;

public class EmailSystem implements Observer {

  private static EmailSystem instance;

  private EmailSystem() {}

  public static EmailSystem getInstance() {
    if (instance == null) {
      instance = new EmailSystem();
    }
    return instance;
  }

  public void update() {
    System.out.println("Emailing order details...");
  }
}
