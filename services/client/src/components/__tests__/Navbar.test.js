import React from "react";
import { shallow } from "enzyme";
import renderer from "react-test-renderer";

import Navbar from "../Navbar";

const title = "Hello, World";

test("Navbar renders properly", () => {
  const wrapper = shallow(<Navbar title={title} />);
  const element = wrapper.find("strong");
  expect(element.length).toBe(1);
  expect(element.get(0).props.children).toBe(title);
});
