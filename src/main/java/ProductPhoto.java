public class ProductPhoto {
    private final String fileLocation;
    private final int width;
    private final int height;

    public ProductPhoto(String fileLocation, int width, int height) {
        this.fileLocation = fileLocation;
        this.width = width;
        this.height = height;
    }

    public String getFileLocation() {
        return fileLocation;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }
}
