import java.math.BigDecimal;
import java.util.List;

public class Item {

  private String name;
  private BigDecimal price;
  private String description;
  private String code;
  private final List<ProductPhoto> productPhotos;

  public Item(
      String name,
      BigDecimal price,
      String description,
      String code,
      List<ProductPhoto> productPhotos) {
    this.name = name;
    this.price = price;
    this.description = description;
    this.code = code;
    this.productPhotos = productPhotos;
  }

  public List<ProductPhoto> getProductPhotos() {
    return productPhotos;
  }

  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }

  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public BigDecimal getPrice() {
    return price;
  }

  public void setPrice(BigDecimal price) {
    this.price = price;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
