public interface Factory {
    Item createItem(
            String name,
            float price,
            String description,
            String code,
            ProductPhoto[] productPhotos
    );
}

