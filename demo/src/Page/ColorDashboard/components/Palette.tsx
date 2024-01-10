import getContrastingColor from "../../../utils/getContrastingColor";
import { SketchPicker } from "react-color";
import * as Menubar from "@radix-ui/react-menubar";

interface Props {
  color: string;
  idx: number;
  updater:(idx:number,hex:string)=>void
}
export default function Palette({ color, idx ,updater}: Props) {
  return (
    <div
      className="flex-1 flex flex-row md:flex-col md:justify-end items-center"
      style={{ backgroundColor: color }}
    >
      <ColorMenu color={color} idx={idx} updater={updater}/>
    </div>
  );
}

function ColorMenu({ color, idx,updater }: Props) {
  function update(hex: string) {
    updater(idx,hex)
  }
  return (
    <Menubar.Root>
      <Menubar.Menu>
        <Menubar.Trigger
          className="font-bold text-2xl mx-3 md:mb-[15rem] px-4 py-2 hover:bg-[#ffffff0d] rounded-lg"
          style={{ color: getContrastingColor(color) }}
        >
          {color}
        </Menubar.Trigger>
        <Menubar.Portal>
          <Menubar.Portal>
            <Menubar.Content>
              <SketchPicker color={color} onChange={(e) => update(e.hex)} />
            </Menubar.Content>
          </Menubar.Portal>
        </Menubar.Portal>
      </Menubar.Menu>
    </Menubar.Root>
  );
}
