import java.math.BigDecimal;
import java.util.List;

public class Notebook extends Item {

  private String size;
  private int pages;

  public Notebook(
      String name,
      BigDecimal price,
      String description,
      String code,
      List<ProductPhoto> productPhotos,
      String size,
      int pages) {
    super(name, price, description, code, productPhotos);
    this.size = size;
    this.pages = pages;
  }

  public String getSize() {
    return size;
  }

  public void setSize(String size) {
    this.size = size;
  }

  public int getPages() {
    return pages;
  }

  public void setPages(int pages) {
    this.pages = pages;
  }
}
