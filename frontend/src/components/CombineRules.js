import React, { useState } from 'react';
import axios from 'axios';

function CombineRules() {
  const [rules, setRules] = useState(['']);
  const [result, setResult] = useState(null);

  const handleRuleChange = (index, value) => {
    const updatedRules = [...rules];
    updatedRules[index] = value;
    setRules(updatedRules);
  };

  const addRule = () => {
    setRules([...rules, '']);
  };

  const combineRules = async () => {
    try {
      const response = await axios.post('http://localhost:5000/combine_rules', { rules });
      setResult(response.data);
    } catch (error) {
      console.error('Error combining rules:', error);
    }
  };

  return (
    <div>
      <h2>Combine Rules</h2>
      {rules.map((rule, index) => (
        <input
          key={index}
          type="text"
          value={rule}
          onChange={(e) => handleRuleChange(index, e.target.value)}
          placeholder="Enter rule"
        />
      ))}
      <button onClick={addRule}>Add Another Rule</button>
      <button onClick={combineRules}>Combine Rules</button>
      {result && <div><strong>Combined AST:</strong> {result}</div>}
    </div>
  );
}

export default CombineRules;
