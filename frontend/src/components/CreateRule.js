import React, { useState } from 'react';
import axios from 'axios';

const CreateRule = () => {
    const [rule, setRule] = useState("");
    const [message, setMessage] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post('/api/create_rule', { rule })
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                setMessage(error.response.data.error || "Error creating rule");
            });
    };

    return (
        <div>
            <h2>Create Rule</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={rule}
                    onChange={(e) => setRule(e.target.value)}
                    placeholder="Enter rule"
                />
                <button type="submit">Submit</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default CreateRule;
