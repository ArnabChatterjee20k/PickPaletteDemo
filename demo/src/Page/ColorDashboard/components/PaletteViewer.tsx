import Palette from "./Palette";
import usePalette from "../../../services/usePalette";

import { useMutation, useQueryClient } from "@tanstack/react-query";

export default function PaletteViewer() {
  const { data: colors } = usePalette();
  const mutation = useMutation({
    mutationFn: ({ idx, hex }: { idx: number; hex: string }) =>
      Promise.resolve({ idx, hex }),
  });
  const client = useQueryClient();
  function updater(idx: number, hex: string) {
    mutation.mutate(
      { idx, hex },
      {
        onSuccess: () => {
          client.setQueryData<string[]>(["palette"], (prev) => {
            if (prev == undefined) return prev;
            const newState = [...prev];
            newState[idx] = hex;
            return newState;
          });
        },
      }
    );
  }
  return (
    <div className="flex flex-col md:flex-row w-full min-h-screen">
      {/* @ts-ignore  */}
      {colors?.map((color, index) => (
        <Palette color={color} key={index} idx={index} updater={updater} />
      ))}
    </div>
  );
}
