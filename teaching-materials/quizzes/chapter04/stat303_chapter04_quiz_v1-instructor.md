# Chapter 4 Quiz: Pandas Fundamentals — Instructor Key

Total: 20 points. Instructor-only; do not publish with student materials.

## Question 1: Labels and positions

Correct answer: **C**. iloc selects positions 1 and 2 and excludes position 3. The labels at those positions are 101 and 107.

## Question 2: Combining conditions

Correct answer: **A**. The required boundaries are >= 8 and < 50000000. Parentheses and & combine the two elementwise comparisons.

## Question 3: Keeping a renamed result

Correct answer: **D**. rename returns a new DataFrame by default. Assigning its result keeps the renamed table without renaming the original.

## Question 4: Choosing a denominator

Correct answer: **B**. The question conditions on an observed rating, so the denominator is 90, not all 100 records.

## Final HTML upload — 16 points

Submit `activity04.html`; follow [Chapter 4 Practice Activity](https://lizhen0909.github.io/stat303-1-sec20-coursebook/pandas_fundamentals.html#practice-activity-select-transform-and-explain).

- **Labels, positions, and object shapes (3 points):** 1 point: predictions and visible selection results; 1: correct label-versus-position explanation; 1: both shapes and Series-versus-DataFrame explanation.

- **Filtering, selected columns, and sorting (4 points):** 1 point: movie import and original shape; 1: correct two-condition mask; 1: explicit copied subset with requested columns and row count; 1: ordered sorting, first five rows, and tie explanation.

- **Calculated variable and retained rename (4 points):** 1 point: correct rowwise difference in millions; 1: displayed results and units; 1: interpretation of negative values and limitation as a profit measure (0.5 each); 1: retained rename, both column-name outputs, and explanation of returned result.

- **Summaries and denominators (4 points):** 1 point: observed-rating subgroup from the full original table; 1: numerator, denominator, guarded ratio; 1: missing-value and subgroup-denominator explanation; 1: median of the renamed gap variable interpreted for selected movies in millions of dollars.

- **Readable completed HTML (1 points):** 0.5 point: name and readable, organized code, outputs, and explanations; 0.5: completion note describing fresh run, save, and HTML inspection. The HTML itself does not prove execution history.
