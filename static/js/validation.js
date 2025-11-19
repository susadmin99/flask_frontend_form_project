// Get the form
const form = document.getElementById("dhsc_east_copy_page_new_signup_form");

// Determine input element + error target based on element structure
function resolveElements(mandatoryEl) {
  let inputEl = null;
  let errorTarget = null;

  // CASE 1: Mandatory class is on a LABEL (normal input/select)
  if (mandatoryEl.tagName.toLowerCase() === "label") {
    inputEl = mandatoryEl.nextElementSibling;

    if (!inputEl) return null;

    // If checkbox, special rule applies
    if (inputEl.type === "checkbox") {
      // Checkbox validation message goes 2 siblings after input
      errorTarget = inputEl.nextElementSibling?.nextElementSibling || null;
    } else {
      // Normal input/select → error is in first next sibling after the input
      errorTarget = inputEl.nextElementSibling || null;
    }
  }

  // CASE 2: Mandatory class is ON the element AFTER checkbox
  else {
    // Checkbox input is the previous sibling
    inputEl = mandatoryEl.previousElementSibling;

    if (!inputEl || inputEl.type !== "checkbox") return null;

    // Checkbox error target = 2nd next sibling of the mandatory element
    errorTarget = mandatoryEl.nextElementSibling?.nextElementSibling || null;
  }

  return { inputEl, errorTarget };
}

// Email check with regex
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Validation for each element
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
      errorTarget.textContent = "Email is not a valid format";
      errorTarget.style.display = "inline-block";
    } else {
      if (mandatoryEl.textContent.length <= 10) {
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

// Live validations
document.querySelectorAll("input, select").forEach((el) => {
  el.addEventListener("input", () => {
    const mandatoryEl =
      el.closest(".form-group-mandatory") ||
      (el.nextElementSibling?.classList?.contains("form-group-mandatory") &&
        el.nextElementSibling) ||
      (el.previousElementSibling?.classList?.contains("form-group-mandatory") &&
        el.previousElementSibling);

    if (mandatoryEl) validateGroup(mandatoryEl);
  });

  el.addEventListener("change", () => {
    const mandatoryEl =
      el.closest(".form-group-mandatory") ||
      (el.nextElementSibling?.classList?.contains("form-group-mandatory") &&
        el.nextElementSibling) ||
      (el.previousElementSibling?.classList?.contains("form-group-mandatory") &&
        el.previousElementSibling);

    if (mandatoryEl) validateGroup(mandatoryEl);
  });
});
