import { SafeAreaView } from "react-native";
import SmartLights from "./components/pages/SmartLights";

export default function App() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: "#151621" }}>
      <SmartLights />
    </SafeAreaView>
  );
}
