import express from 'express';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

dotenv.config();
const app = express();
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const PORT = 5173;

// Статика
app.use(express.static(path.join(__dirname, 'public')));

// Роуты
app.get('/docs', (_, res) => {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});

app.get('/tracker', (_, res) => {
  res.sendFile(path.join(__dirname, 'public/tracker.html'));
});

// Запуск
app.listen(PORT, () => {
  console.log(`Frontend running on http://localhost:${PORT}`);
});
