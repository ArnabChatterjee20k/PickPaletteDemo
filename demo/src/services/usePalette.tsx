import { useQuery } from "@tanstack/react-query";
const colors = ["#242038", "#9067C6", "#8D86C9", "#BDAFC7", "#F7ECE1"];
import { PALETTE_URL } from "../config";
async function fetcher(){
  const res = await fetch(PALETTE_URL)
  const data:string[] = await res.json()
  return data
}
export default function usePalette() {
  return useQuery({
    queryKey: ["palette"],
    queryFn: fetcher,
  });
}
