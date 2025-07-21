# How to Remember Selection, Insertion, and Bubble Sort

Here are some simple ways to remember the difference between Selection, Insertion, and Bubble Sort.

The key is to associate each one with a single, core action.

### 1. Selection Sort: "Select the Minimum"

Think of it as finding the best and putting it in its place.

*   **Core Idea:** Scan the entire unsorted part of the array to **find the absolute minimum** element, then swap it into the first available position.
*   **Analogy:** Imagine you have a line of people and you want to sort them by height. You would look at everyone in the line, find the shortest person, and send them to the very beginning. Then you'd ignore them and repeat the process for the rest of the line.
*   **In short:** **Select** the minimum and swap.

### 2. Insertion Sort: "Insert Like a Card"

Think of sorting a hand of playing cards.

*   **Core Idea:** You build a sorted section of the array. You take the next unsorted element and **insert it into the correct spot** within the already sorted section by shifting other elements over.
*   **Analogy:** You're holding a few sorted cards in your hand. You draw a new card. You slide it into your hand, moving it past the other cards until you find its correct place.
*   **In short:** Take the next item and **insert** it into the sorted part.

### 3. Bubble Sort: "Swap with Your Neighbor"

Think of the largest elements "bubbling up" to the end of the array.

*   **Core Idea:** Repeatedly step through the list, comparing **adjacent (neighboring) elements**, and swap them if they're in the wrong order.
*   **Analogy:** The biggest bubbles in a fizzy drink rise to the top. In each pass, the largest unsorted element "bubbles up" towards its final position at the end of the array. This happens through many small, local swaps.
*   **In short:** **Swap** with your neighbor if you're out of order.

---

### Quick Summary Table

| Algorithm | Core Action | Key Phrase to Remember |
| :--- | :--- | :--- |
| **Selection Sort** | Finds the smallest element and puts it at the beginning. | "Select the best, move it to the front." |
| **Insertion Sort** | Takes an element and inserts it into the sorted part. | "Insert a card into a sorted hand." |
| **Bubble Sort** | Swaps adjacent elements. | "Swap with your neighbor." |
