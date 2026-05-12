import os
import zipfile

# Define project structure and file contents
project_name = "pizza-parlor"
structure = {
    "pom.xml": """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.pizzaparlor</groupId>
    <artifactId>pizza-parlor</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.8.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>""",
    "README.md": """# 🍕 Pizza Parlor — Java OOP Practice Assessment

## Implementation Steps
1. Implement `Topping.java`
2. Implement `PizzaRecipe.java` (Use Defensive Copying)
3. Implement `PizzaOrder.java` and `OrderStatus.java`
4. Implement `PizzaOven.java` (Abstract)
5. Implement `WoodFiredOven.java` and `ElectricOven.java`

Run tests with: `mvn test`""",
    "practice_answers.txt": """# Long Question Answer
[Your answer here regarding Defensive Copying and Encapsulation]""",
    "src/main/java/com/pizzaparlor/Main.java": "package com.pizzaparlor;\n\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Welcome to the Pizza Parlor!\");\n    }\n}",
    "src/main/java/com/pizzaparlor/model/Topping.java": "package com.pizzaparlor.model;\n\npublic class Topping {\n    // TODO: Implement fields, constructor, and methods\n}",
    "src/main/java/com/pizzaparlor/model/PizzaRecipe.java": "package com.pizzaparlor.model;\n\nimport java.util.*;\n\npublic class PizzaRecipe {\n    // TODO: Implement fields, constructor, and methods (Use Defensive Copying)\n}",
    "src/main/java/com/pizzaparlor/model/PizzaOrder.java": "package com.pizzaparlor.model;\n\npublic class PizzaOrder {\n    // TODO: Implement order lifecycle logic\n}",
    "src/main/java/com/pizzaparlor/model/OrderStatus.java": "package com.pizzaparlor.model;\n\npublic enum OrderStatus {\n    WAITING, BAKING, READY\n}",
    "src/main/java/com/pizzaparlor/service/PizzaOven.java": "package com.pizzaparlor.service;\n\nimport com.pizzaparlor.model.*;\nimport java.util.*;\n\npublic abstract class PizzaOven {\n    // TODO: Implement menu and queue management\n    protected abstract void performBake(PizzaOrder order);\n}",
    "src/main/java/com/pizzaparlor/service/WoodFiredOven.java": "package com.pizzaparlor.service;\n\nimport com.pizzaparlor.model.PizzaOrder;\n\npublic class WoodFiredOven extends PizzaOven {\n    @Override\n    protected void performBake(PizzaOrder order) {\n        // TODO: Implement specific print statement\n    }\n}",
    "src/main/java/com/pizzaparlor/service/ElectricOven.java": "package com.pizzaparlor.service;\n\nimport com.pizzaparlor.model.PizzaOrder;\n\npublic class ElectricOven extends PizzaOven {\n    @Override\n    protected void performBake(PizzaOrder order) {\n        // TODO: Implement specific print statement\n    }\n}",
    "src/test/java/com/pizzaparlor/ToppingTest.java": "package com.pizzaparlor;\n\npublic class ToppingTest {\n    // Add JUnit tests here\n}",
}

zip_filename = "pizza-parlor-practice.zip"

with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for path, content in structure.items():
        zipf.writestr(os.path.join(project_name, path), content)

print(f"Zip file created: {zip_filename}")