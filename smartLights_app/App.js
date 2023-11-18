import { StatusBar } from "expo-status-bar";
import { SafeAreaView } from "react-native";
import SmartLights from "./components/pages/SmartLights";

export default function App() {
  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: "#151621", zIndex: 0 }}>
      <SmartLights />
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}
