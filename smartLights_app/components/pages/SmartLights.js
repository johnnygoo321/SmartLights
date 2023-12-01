import React, { useState } from "react";
import { Dimensions, View, FlatList } from "react-native";
import { ColorPicker, fromHsv } from "react-native-color-picker";
import { IPV4_ADDRESS_OF_PI, SERVER_PORT } from "@env";
import Toast from "react-native-toast-message";
import ToastConfig from "../configurations/toastConfig";
import axios from "axios";
import Slider from "@react-native-community/slider";
import hexRgb from "hex-rgb";
import RoundedButton from "../buttons/RoundedButton";

const { width, height } = Dimensions.get("window");

const SmartLights = () => {
  //State referencing current color of strip and if an animation is currently in effect
  const [rgbValue, setRgbValue] = useState({ red: 255, green: 118, blue: 0 });
  const [loading, setLoadingState] = useState(false);

  //Different animation effects, this list can be expanded to include many more animations
  const effects = [
    { effect: "wipe" },
    { effect: "comet" },
    { effect: "rainbow" },
    { effect: "rainbowCycle" },
    { effect: "sparkle" },
    { effect: "theaterChase" },
    { effect: "theaterChaseRainbow" },
    { effect: "randomize" },
    { effect: "off" },
  ];

  const configureLedStrip = async (endpoint) => {
    let baseUrl = IPV4_ADDRESS_OF_PI + ":" + SERVER_PORT + "/" + endpoint,
      data = { red: rgbValue.red, green: rgbValue.green, blue: rgbValue.blue };

    setLoadingState(true);
    Toast.show({
      type: "info",
      text1: "Processing Request",
      text2: "Please wait...",
      autoHide: false,
    });

    await axios
      .post(baseUrl, data, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      })
      .then(
        (response) => {
          console.log(response);
          setLoadingState(false);
          Toast.show({
            type: "success",
            text1: response.data,
            text2: "Animation Selected: " + endpoint,
            visibilityTime: 2500,
          });
        },
        (error) => {
          console.log("Miserable Failure Error: ", error);
          setLoadingState(false);
          Toast.show({
            type: "error",
            text1: "Could not configure LED Strip.",
            text2: "Check Error logs...",
            visibilityTime: 2500,
          });
        }
      );
  };

  return (
    <View style={{ flex: 1, alignItems: "center" }} pointerEvents={loading}>
      <View style={{ zIndex: 1 }}>
        <Toast config={ToastConfig} />
      </View>
      <View
        style={{
          zIndex: 0,
        }}
      >
        <ColorPicker
          sliderComponent={Slider}
          hideSliders={true}
          defaultColor={"orange"}
          onColorSelected={() => configureLedStrip("noEffect")}
          onColorChange={(color) => setRgbValue(hexRgb(fromHsv(color)))}
          style={{ width: width, height: height / 2.4 }}
        />
      </View>
      <View style={{ flex: 1 }}>
        <FlatList
          data={effects}
          renderItem={({ item }) => (
            <RoundedButton
              onPress={() => configureLedStrip(item.effect)}
              buttonText={
                item.effect.charAt(0).toUpperCase() + item.effect.slice(1)
              }
            ></RoundedButton>
          )}
          keyExtractor={(item) => item.effect}
        />
      </View>
    </View>
  );
};

export default SmartLights;
