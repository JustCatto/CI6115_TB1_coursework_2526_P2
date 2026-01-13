plugins {
    id("java")
    id("com.diffplug.spotless") version "8.1.0"
}

group = "org.kingston.ac.uk"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

tasks.test {
    useJUnitPlatform()
}

spotless {
    java {
        importOrder()
        removeUnusedImports()
        forbidWildcardImports()
        forbidModuleImports()
        googleJavaFormat()
        formatAnnotations()  // fixes type annotation formatting
    }

    python {
        target("python/src/**/*.py")
        black("25.12.0").pathToExe("C:\\Users\\Romvulus Casunuran\\IdeaProjects\\Cl6116_TB1_coursework_2526_P2\\python\\.venv\\Scripts\\black.exe")
    }
}