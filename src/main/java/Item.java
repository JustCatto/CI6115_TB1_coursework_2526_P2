public abstract class Item {

  private String name;
  private float price;
  private String description;
  private String code;
  private final ProductPhoto[] productPhotos;

  public Item(
          String name,
          float price,
          String description,
          String code,
          ProductPhoto[] productPhotos) {
    this.name = name;
    this.price = price;
    this.description = description;
    this.code = code;
    this.productPhotos = productPhotos;
  }

  public ProductPhoto[] getProductPhotos() {
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

  public float getPrice() {
    return price;
  }

  public void setPrice(float price) {
    this.price = price;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
