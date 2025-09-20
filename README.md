# pointbiserial
point biserial correlation coefficient
The point biserial correlation coefficient (rpb) is a correlation coefficient used when one variable (e.g. Y) is dichotomous; Y can either be "naturally" dichotomous, like whether a coin lands heads or tails, or an artificially dichotomized variable. In most situations it is not advisable to dichotomize variables artificially. When a new variable is artificially dichotomized the new dichotomous variable may be conceptualized as having an underlying continuity. If this is the case, a biserial correlation would be the more appropriate calculation.

The point-biserial correlation is mathematically equivalent to the Pearson (product moment) correlation coefficient; that is, if we have one continuously measured variable X and a dichotomous variable Y, rXY = rpb. This can be shown by assigning two distinct numerical values to the dichotomous variable.

The computational steps in this small program are based on Bruning & Kintz, Computational Handbook of Statistics

Simply run the Python code and load the data from the csv file matrix.csv

Obviously, modern statistical packages can compute rpb using built-in libraries, the present code is for those that wish to verify Bruning & Kintz's distinct computational steps.
