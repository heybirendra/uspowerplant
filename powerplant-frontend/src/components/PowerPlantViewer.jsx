import React, { useState, useEffect } from 'react';
import axios from "axios";

export default function PowerPlantViewer() {
  const [states, setStates] = useState([]);
  const [selectedState, setSelectedState] = useState("");
  const [limit, setLimit] = useState(10);
  const [plants, setPlants] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch distinct states from API
    axios.get(`${process.env.REACT_APP_API_URL}/pp/states`)
      .then((res) => {
          console.log("States API response:", res.data);
        setStates(res.data);
        setSelectedState(res.data[0]); // Set first state as default
      })
      .catch((err) => console.error("Failed to fetch states", err));
  }, []);

  useEffect(() => {
    if (selectedState) {
      axios.get(`${process.env.REACT_APP_API_URL}/pp/powerplants`, {
        params: { limit, state: selectedState }
      }).then((res) => {
        setPlants(res.data);
      });
    }
  }, [selectedState, limit]);

//   const fetchPlants = async () => {
//     if (!selectedState) {
//       setPlants([]);
//       return;
//     }
//     setLoading(true);
//     setError(null);
//     try {
//       const response = await fetch(`pp/powerplants?state=${selectedState}&limit=${limit}`);
//       if (!response.ok) throw new Error('Failed to fetch');
//       const data = await response.json();
//       setPlants(data);
//     } catch (err) {
//       setError(err.message);
//     }
//     setLoading(false);
//   };
//
//
//
//
//   // Fetch whenever selectedState or limit changes
//   useEffect(() => {
//     fetchPlants();
//   }, [selectedState, limit]);

  return (
    <div style={{ maxWidth: 800, margin: 'auto', padding: 20 }}>
      <h2>Power Plant Viewer</h2>

      <div style={{ marginBottom: 20 }}>
        <label>
          Select State:
          <select
            value={selectedState}
            onChange={e => setSelectedState(e.target.value)}
            style={{ marginLeft: 10 }}
          >
            <option value="">--Choose a state--</option>
            {states.map(state => (
              <option key={state} value={state}>{state}</option>
            ))}
          </select>
        </label>
      </div>

      <div style={{ marginBottom: 20 }}>
        <label>
          Number of Plants to View:
          <input
            type="number"
            min="1"
            max="100"
            value={limit}
            onChange={e => setLimit(Number(e.target.value))}
            style={{ marginLeft: 10, width: 60 }}
          />
        </label>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {!loading && plants.length > 0 && (
        <table border="1" cellPadding="8" style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
                <th>State</th>
              <th>Plant Name</th>
              <th>Net Generation (MWh)</th>
            </tr>
          </thead>
          <tbody>
            {plants.map(plant => (
              <tr key={plant.plant_id}>
                  <td>{plant.state}</td>
                <td>{plant.plant_name}</td>

                <td>{plant.net_generation_mwh}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {!loading && plants.length === 0 && selectedState && <p>No power plants found for this state.</p>}
    </div>
  );
}
