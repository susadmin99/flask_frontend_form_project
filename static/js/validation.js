const form = document.getElementById("dhsc_east_copy_page_new_signup_form");

//This function resolves the element if it is a select, input, label or an error span
function resolveElements(mandatoryEl) {
  let inputEl = null;
  let errorTarget = null;

  if (mandatoryEl.tagName.toLowerCase() === "label") {
    inputEl = mandatoryEl.nextElementSibling;

    if (!inputEl) return null;

    if (inputEl.type === "checkbox") {
      errorTarget = inputEl.nextElementSibling?.nextElementSibling || null;
    } else {
      let sibling = inputEl.nextElementSibling;

      while (sibling) {
        if (sibling.tagName.toLowerCase() === "span") {
          break;
        }
        sibling = sibling.nextElementSibling;
      }
      errorTarget = sibling || null;
    }
  } else {
    inputEl = mandatoryEl.previousElementSibling;

    if (!inputEl || inputEl.type !== "checkbox") return null;

    errorTarget = mandatoryEl.nextElementSibling?.nextElementSibling || null;
  }

  return { inputEl, errorTarget };
}

//Email check with regex
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

//Validation for each element
//First resolves what element is it and continues with checking the value of the input field or the select or if the element is email checks the email format
function validateGroup(mandatoryEl) {
  const resolved = resolveElements(mandatoryEl);
  if (!resolved) return true;

  const { inputEl, errorTarget } = resolved;
  if (!errorTarget) return true;

  let isValid = true;

  if (inputEl.tagName.toLowerCase() === "input") {
    if (inputEl.type === "checkbox") {
      isValid = inputEl.checked;
    } else if (inputEl.type === "email") {
      const value = inputEl.value.trim();
      isValid = value !== "" && isValidEmail(value);
    } else {
      isValid = inputEl.value.trim() !== "";
    }
  }

  if (inputEl.tagName.toLowerCase() === "select") {
    isValid = inputEl.value.trim() !== "";
  }

  if (isValid) {
    errorTarget.textContent = "";
    errorTarget.style.display = "none";
  } else {
    if (inputEl.type === "email") {
      //Custom check for the email input if the format is incorrect
      errorTarget.textContent = "Email is not a valid format";
      errorTarget.style.display = "inline-block";
    } else {
      if (mandatoryEl.textContent.length <= 10) {
        //Check if the label has longer name length than 10 characters then use simple response if less or equal 10 then use the label also with custom message
        errorTarget.textContent =
          mandatoryEl.textContent + " is a required field";
      } else {
        errorTarget.textContent = "It is a required field";
      }
      errorTarget.style.display = "inline-block";
    }
  }

  return isValid;
}

//Get all of the elements with mandatory classes and validate each one by one
function validateAll() {
  const mandatoryEls = document.querySelectorAll(".form-group-mandatory");
  let allValid = true;

  mandatoryEls.forEach((el) => {
    if (!validateGroup(el)) allValid = false;
  });

  return allValid;
}

form.addEventListener("submit", (e) => {
  if (!validateAll()) {
    e.preventDefault();
  } else {
    console.log("form submitted");
  }
});

//Live validations
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("label.form-group-mandatory").forEach((label) => {
    const input = label.nextElementSibling; // input immediately after label

    if (!input) return;

    input.addEventListener("input", () => {
      const span = input.nextElementSibling;

      if (span && span.tagName.toLowerCase() === "span") {
        if (input.value.trim() !== "") {
          validateGroup(label);
        }
      }
    });
  });

  document.querySelectorAll("b.form-group-mandatory").forEach((b) => {
    const input = b.previousElementSibling; // input directly before <b>

    if (!input || input.type !== "checkbox") return;

    input.addEventListener("change", () => {
      const span = b.nextElementSibling.nextElementSibling;

      if (span && span.tagName.toLowerCase() === "span") {
        if (input.checked) {
          span.textContent = "";
          span.style.display = "none";
        }
      }
    });
  });
});
