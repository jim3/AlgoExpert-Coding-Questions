```js
// class definition
class Person {
    constructor(firstName, lastName) {
        // capture firstName param into this.firstName instance variable
        this.firstName = firstName;
        // capture lastName param into this.lastName instance variable
        this.lastName = lastName;
    }
}

// class usage
const person = new Person("Sam", "Green");
```
---

```js
class Rectangle {
    /**
     * @param {number} width
     * @param {number} height
     */
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
}

const makeSquare = () => {
    // TODO: return a new instance of Rectangle with same width and height
    // example: 10 for width and 10 for height
    return new Rectangle(5, 5);
};

// Sample usage - do not modify
console.log(makeSquare());
```

---

```js
class Translation {
       constructor(word) {
            // Capture constructor param into an instance variable
            // This is explained in the next lesson
            this.word = word;
       }
       
       isEnglishWord() {
            // returns true when word is English, false otherwise
       }

       isSpanishWord() {
            // returns true when word is Spanish, false otherwise
       }
}

const person1 = new Person("Sam Doe");
const person2 = new Person("Charley Bron");
```
