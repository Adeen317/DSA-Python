# Data Structures and Algorithm-Python

#### Linear Search-BruteForce
##### Q. Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number b turning over as few cards as possible. Write a function to help Bob locate the card.

##### Test Cases

Below are the test cases used for validating the function:

1. **Test Case 1**  
   - **Input:** `cards = [13, 11, 10, 7, 4, 3, 1, 0]`, `query = 7`
   - **Output:** `3`

2. **Test Case 2**  
   - **Input:** `cards = [4, 2, 1, -1]`, `query = 4`
   - **Output:** `0`

3. **Test Case 3**  
   - **Input:** `cards = [3, -1, -9, -127]`, `query = -127`
   - **Output:** `3`

4. **Test Case 4**  
   - **Input:** `cards = [13]`, `query = 13`
   - **Output:** `0`

5. **Test Case 5**  
   - **Input:** `cards = [13, 11, 10, 7, 4, 3, 1, 0]`, `query = 5`
   - **Output:** `-1`

6. **Test Case 6**  
   - **Input:** `cards = []`, `query = 7`
   - **Output:** `-1`

7. **Test Case 7**  
   - **Input:** `cards = [13, 13, 11, 10, 10, 7, 4, 3, 1, 0]`, `query = 7`
   - **Output:** `5`

8. **Test Case 8**  
   - **Input:** `cards = [13, 11, 10, 7, 7, 7, 4, 3, 1, 0]`, `query = 7`
   - **Output:** `3`

