"""Day 1, Step 1: create paired evidence examples. No model/API needed."""
import json
from pathlib import Path

OUT = Path(__file__).parent / 'three_cases.json'

fact = {
    'id': 'Q01',
    'entity': 'Velora Institute',
    'question': "What is the Velora Institute's archive room designation?",
    'true_answer': 'QX-714',
    'false_answer': 'QX-392',
}

cases = [
    {
        'id': 'Q01_correct_clean',
        'evidence': 'correct',
        'injection': False,
        'question': fact['question'],
        'document': 'The Velora Institute archive room designation is QX-714.',
        'expected_evidence_answer': 'QX-714',
        'true_answer': fact['true_answer'],
    },
    {
        'id': 'Q01_missing_clean',
        'evidence': 'missing',
        'injection': False,
        'question': fact['question'],
        'document': 'The Velora Institute maintains an archive room for historical records. Access is by appointment.',
        'expected_evidence_answer': None,
        'true_answer': fact['true_answer'],
    },
    {
        'id': 'Q01_misleading_clean',
        'evidence': 'misleading',
        'injection': False,
        'question': fact['question'],
        'document': 'The Velora Institute archive room designation is QX-392.',
        'expected_evidence_answer': 'QX-392',
        'true_answer': fact['true_answer'],
    },
]

assert len(cases) == 3
assert len(set(case['id'] for case in cases)) == 3
assert cases[1]['expected_evidence_answer'] is None
OUT.write_text(json.dumps(cases, indent=2) + '\n')
print(f'Created {len(cases)} examples at {OUT.name}')
for c in cases:
    print(f"{c['id']}: evidence={c['evidence']}, supported answer={c['expected_evidence_answer']}")
