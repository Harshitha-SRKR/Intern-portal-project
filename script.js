document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('intern-name')) {
    fetch('/api/user')
      .then(res => res.json())
      .then(data => {
        document.getElementById('intern-name').textContent = data.name;
        document.getElementById('referral-code').textContent = data.referral_code;
        document.getElementById('donations').textContent = data.total_donations;
      });
  }

  if (document.getElementById('leaderboard-table')) {
    fetch('/api/leaderboard')
      .then(res => res.json())
      .then(data => {
        const tbody = document.querySelector('#leaderboard-table tbody');
        data.forEach(item => {
          const row = `<tr><td>${item.name}</td><td>${item.donations}</td></tr>`;
          tbody.innerHTML += row;
        });
      });
  }
});
