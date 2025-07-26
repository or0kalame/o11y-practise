// frontend.js
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(__dirname));

app.get('/', (_, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(8002, () => {
  console.log('Frontend running at http://localhost:8002');
});
