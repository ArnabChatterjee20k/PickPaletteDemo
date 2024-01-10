import usePalette from "../../services/usePalette";
const Demo = () => {
  function handler(){
    alert("Its pick pallet buddy")
  }
  const { data: palette, isLoading } = usePalette();
  if (isLoading || !palette) return <h1>Loading..........</h1>;
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
      }}
    >
      <button
        onClick={() => handler()}
        style={{
          backgroundColor: palette[0],
          color: "#fff",
          margin: "10px",
          padding: "15px 20px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Button 1
      </button>
      <button
        onClick={() => handler()}
        style={{
          backgroundColor: palette[1],
          color: "#fff",
          margin: "10px",
          padding: "15px 20px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Button 2
      </button>
      <button
        onClick={() => handler()}
        style={{
          backgroundColor: palette[2],
          color: "#fff",
          margin: "10px",
          padding: "15px 20px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Button 3
      </button>
      <button
        onClick={() => handler()}
        style={{
          backgroundColor: palette[3],
          color: "#fff",
          margin: "10px",
          padding: "15px 20px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Button 4
      </button>
      <button
        onClick={() => handler()}
        style={{
          backgroundColor: palette[4],
          color: "#fff",
          margin: "10px",
          padding: "15px 20px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px",
          fontWeight: "bold",
        }}
      >
        Button 5
      </button>
    </div>
  );
};

export default Demo;
