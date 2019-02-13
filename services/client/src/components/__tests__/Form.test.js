import React from "react";
import { shallow } from "enzyme";
import renderer from "react-test-renderer";

import Form from "../Form";

const testData = [
  {
    formType: "Register",
    title: "Register",
    formData: {
      username: "",
      email: "",
      password: ""
    }
  },
  {
    formType: "Login",
    title: "Log In",
    formData: {
      email: "",
      password: ""
    }
  }
];

describe("When not authenticated", () => {
  testData.forEach(el => {
    test(`${el.formType} Form renders properly`, () => {
      const component = <Form formType={el.formType} formData={el.formData} />;
      const wrapper = shallow(component);
      const h1 = wrapper.find("h1");
      expect(h1.length).toBe(1);
      expect(h1.get(0).props.children).toBe(el.formType);
      const formGroup = wrapper.find(".field");
      expect(formGroup.length).toBe(Object.keys(el.formData).length);
      expect(formGroup.get(0).props.children.props.name).toBe(
        Object.keys(el.formData)[0]
      );
      expect(formGroup.get(0).props.children.props.value).toBe("");
    });

    test(`${el.formType} Form renders a snapshot properly`, () => {
      const component = <Form formType={el.formType} formData={el.formData} />;
      const tree = renderer.create(component).toJSON();
      expect(tree).toMatchSnapshot();
    });
  });
});

describe("When authenticated", () => {
  testData.forEach(el => {
    const component = (
      <Form
        formType={el.formType}
        formData={el.formData}
        isAuthenticated={true}
      />
    );
    it(`${el.formType} redirects properly`, () => {
      const wrapper = shallow(component);
      expect(wrapper.find("Redirect")).toHaveLength(1);
    });
  });
});
