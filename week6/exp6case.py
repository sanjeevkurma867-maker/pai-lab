from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'IncomeStability': ['Stable', 'Stable', 'Unstable', 'Stable', 'Unstable', 'Stable', 'Unstable', 'Stable'],
    'CreditHistory': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad'],
    'EmploymentType': ['Salaried', 'Self-employed', 'Unemployed', 'Salaried', 'Self-employed', 'Salaried', 'Unemployed', 'Self-employed'],
    'DefaultRisk': ['Low', 'High', 'High', 'Low', 'High', 'Low', 'High', 'High']
})

# Define Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('EmploymentType', 'IncomeStability'),
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk')
])

# Train the model
model.fit(data)

# Inference
inference = VariableElimination(model)

# Example query with incomplete data
result = inference.query(
    variables=['DefaultRisk'],
    evidence={
        'CreditHistory': 'Good',
        'EmploymentType': 'Salaried'
        # IncomeStability is unknown
    }
)

print(result)
