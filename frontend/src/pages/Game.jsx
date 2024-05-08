import {useState, useEffect} from "react";
import axios from "axios";
import styles from "./Game.module.css"; // Importing the CSS module

const Game = () => {
  const [board, setBoard] = useState([]);
  const [turn, setTurn] = useState(0);
  const [winner, setWinner] = useState(-1);
  const cellColor = (value) => {
    switch (value) {
      case 0:
        return styles.cellBlue;
      case 1:
        return styles.cellRed;
      default:
        return "";
    }
  };

  useEffect(() => {
    axios.get("http://localhost:8080/api/board").then((response) => {
      setBoard(response.data.board);
    });
  }, []);

  async function move(column) {
    try {
      const response = await axios.post("http://localhost:8080/api/move", {
        column: column,
        playerID: turn,
      });
      setBoard(response.data.board);
      setTurn(response.data.turn);
      setWinner(response.data.winner);
    } catch (error) {
      console.error(error);
    }
  }

  async function reset() {
    await axios.get("http://localhost:8080/api/reset").then((response) => {
      setBoard(response.data.board);
      setTurn(response.data.turn);
      setWinner(-1);
    });
  }

  return (
    <>
      <div>
        <div className={styles.container}>
          <h1>Connect 4</h1>
          <h2>Player {turn + 1}&apos;s turn</h2>
          <table>
            <tbody>
              {board.map((row, rowIndex) => (
                <tr key={rowIndex}>
                  {row.map((cell, columnIndex) => (
                    <td
                      key={columnIndex}
                      className={`${styles.cell} ${cellColor(cell)}`}
                      onClick={() => move(columnIndex)}
                    ></td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {winner !== -1 && <h2>Player {winner + 1} wins!</h2>}
          <button className={styles.reset} onClick={reset}>
            Reset
          </button>
        </div>
      </div>
    </>
  );
};

export default Game;
