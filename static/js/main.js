document.getElementById('ruleForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const user_id = document.getElementById('user_id').value;
    const rule = document.getElementById('rule').value;

    const data = {
        user_id: parseInt(user_id),
        rule: rule
    };

    fetch('/check_eligibility', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        if (data.eligible) {
            resultDiv.innerHTML = `<p>User is eligible based on rule: ${data.rule}</p>`;
            resultDiv.style.color = 'green';
        } else {
            resultDiv.innerHTML = `<p>User is NOT eligible based on rule: ${data.rule}</p>`;
            resultDiv.style.color = 'red';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
