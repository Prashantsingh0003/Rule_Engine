import React, { useState } from 'react';
import axios from 'axios';

const EvaluateRule = () => {
    const [ruleId, setRuleId] = useState("");
    const [userData, setUserData] = useState({});
    const [result, setResult] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post('/api/evaluate_rule', {
            rule_id: ruleId,
            data: userData
        })
            .then(response => {
                setResult(response.data.result ? "Rule Passed!" : "Rule Failed!");
            })
            .catch(error => {
                setResult(error.response.data.error || "Error evaluating rule");
            });
    };

    return (
        <div>
            <h2>Evaluate Rule</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={ruleId}
                    onChange={(e) => setRuleId(e.target.value)}
                    placeholder="Enter Rule ID"
                />
                <textarea
                    placeholder="Enter user data as JSON"
                    onChange={(e) => setUserData(JSON.parse(e.target.value))}
                />
                <button type="submit">Evaluate</button>
            </form>
            {result && <p>{result}</p>}
        </div>
    );
};

export default EvaluateRule;
