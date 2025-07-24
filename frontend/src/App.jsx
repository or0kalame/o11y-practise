// src/App.jsx
import { useState } from 'react';
import axios from 'axios';
import './App.css';

function generateTrackingNumber() {
  return 'TRK' + Math.floor(Math.random() * 1000000);
}

function App() {
  const [form, setForm] = useState({
    tracking_number: generateTrackingNumber(),
    status: 'formed',
    warehouse_id: '',
    item_name: '',
  });
  const [getTracking, setGetTracking] = useState('');
  const [result, setResult] = useState(null);

  const handleAdd = async () => {
    try {
      await axios.post('http://localhost:8000/add_package', form);
      alert('Посылка добавлена!');
      setForm({
        tracking_number: generateTrackingNumber(),
        status: 'formed',
        warehouse_id: '',
        item_name: '',
      });
    } catch (err) {
      alert('Ошибка при добавлении');
    }
  };

  const handleGet = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/get?tracking_number=${getTracking}`);
      setResult(res.data);
    } catch (err) {
      alert('Посылка не найдена');
    }
  };

  return (
    <div className="container">
      <h1>Добавить посылку</h1>
      <div className="form-group">
        <input disabled value={form.tracking_number} />
        <input value={form.status} disabled />
        <input placeholder="Номер склада" value={form.warehouse_number} onChange={e => setForm({ ...form, warehouse_number: e.target.value })} />
        <input placeholder="Название товара" value={form.product_name} onChange={e => setForm({ ...form, product_name: e.target.value })} />
        <button onClick={handleAdd}>Добавить</button>
      </div>

      <h2>Получить посылку</h2>
      <div className="form-group">
        <input placeholder="Трек-номер" value={getTracking} onChange={e => setGetTracking(e.target.value)} />
        <button onClick={handleGet}>Найти</button>
      </div>

      {result && (
        <div className="result">
          <p><b>Статус:</b> {result.status}</p>
          <p><b>Склад:</b> {result.warehouse_number}</p>
          <p><b>Товар:</b> {result.product_name}</p>
        </div>
      )}
    </div>
  );
}

export default App;
