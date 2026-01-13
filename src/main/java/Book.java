import java.math.BigDecimal;
import java.util.List;

public class Book extends Item {

  private int Pages;
  private String publisher;
  private List<String> authors;

  public Book(
      String name,
      BigDecimal price,
      String description,
      String code,
      List<ProductPhoto> productPhotos,
      int pages,
      String publisher,
      List<String> authors) {
    super(name, price, description, code, productPhotos);
    Pages = pages;
    this.publisher = publisher;
    this.authors = authors;
    if (authors.isEmpty()) {
      throw new IllegalArgumentException("Book must have at least 1 author.");
    }
  }
}
