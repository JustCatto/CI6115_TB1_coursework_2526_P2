import java.math.BigDecimal;
import java.util.List;

public class Magazine extends Item {

  private int Pages;
  private String Publisher;

  public Magazine(
      String name,
      BigDecimal price,
      String description,
      String code,
      List<ProductPhoto> productPhotos,
      int pages,
      String publisher) {
    super(name, price, description, code, productPhotos);
    Pages = pages;
    Publisher = publisher;
  }

  public int getPages() {
    return Pages;
  }

  public void setPages(int pages) {
    Pages = pages;
  }

  public String getPublisher() {
    return Publisher;
  }

  public void setPublisher(String publisher) {
    Publisher = publisher;
  }
}
