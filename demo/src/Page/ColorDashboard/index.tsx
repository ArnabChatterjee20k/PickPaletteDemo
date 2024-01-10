import { useMutation } from "@tanstack/react-query";
import Logo from "../../components/Logo";
import PaletteViewer from "./components/PaletteViewer";
import usePalette from "../../services/usePalette";
import { PALETTE_URL } from "../../config";
async function changeColor(colors: string[]) {
  const headersList = {
    "Content-Type": "application/json",
  };
  const bodyContent = JSON.stringify({colors});

  const res = await fetch(PALETTE_URL, {
    method: "PUT",
    body: bodyContent,
    headers: headersList,
  });
  return res.status;
}

export default function index() {
  const mutate = useMutation({
    mutationFn: (colors: string[]) => changeColor(colors),
  });
  const {isPending} = mutate
  const { data: palette } = usePalette();
  function handleClick() {
    if (!palette) return;
    mutate.mutate(palette, {
      onSuccess: () => {
        alert("success");
      },
    });
  }
  return (
    <section>
      <div className="w-full my-3 px-3 flex justify-between">
        <Logo />
        <button
          className="px-4 py-2 bg-black text-white rounded mx-5"
          onClick={handleClick}
          disabled={isPending}
        >
          {isPending?"Loading...":"Update"}
        </button>
      </div>
      <PaletteViewer />
    </section>
  );
}
