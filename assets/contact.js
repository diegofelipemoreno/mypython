import * as contactView from '../view/contactView.js';
import * as utils from '../../../../utils/utils.js';
import {bookAppServices} from '../../../../appServices.js';
import {isValidEmail,
  isValidWordCharacter} from '../../../../utils/valid-form-fields.js';

/**
 * Contact Component
 * @return {object}
 */
export class Contact {
  /**
   * @param {Element} element DOM element.
   */
  constructor(element) {
    /**
     * Component selector
     */
    this.element = document.querySelector(element);

    /**
    * Service object data
    */
    this.bookAppServices = bookAppServices();

    /**
     * Form selector
     */
    this.contactForm = {};

    /**
     * Form input selectors
     */
    this.formInputs = {};

    /**
     * Model Form data
     */
    this.modelFormData = {
      'name': ['', false],
      'email': ['', false],
      'message': ['', false]
    };

    /**
     * Form data state
     */
    this.stateForm = this.modelFormData;

    /**
     * check if data setted is valid (boolean)
     */
    this.isValidData = this.isValidData_() || false;
  }


  /**
  * Reset form
  * @private
  */
  resetForm_() {
    const succedMessageContainer =
      this.element.querySelector(Selectors.MESSAGE_SUCCED),
      formContainer = this.element.querySelector(Selectors.FORM_CONTAINER);

    this.stateForm = this.modelFormData;
    succedMessageContainer.classList.toggle(Classname.DISABLED);
    formContainer.classList.toggle(Classname.DISABLED);
    Array.from(this.formInputs, (elem) => elem.value = '');
  }

  /**
  * Setting / update form state
  * @private
  */
  setFormState() {
    const contactName = this.element.querySelector(Selectors.CONTACT_NAME),
      contactEmail = this.element.querySelector(Selectors.CONTACT_EMAIL),
      contactMessage = this.element.querySelector(Selectors.CONTACT_MESSAGE);

    this.stateForm['name'][0] = contactName.value;
    this.stateForm['email'][0] = contactEmail.value;
    this.stateForm['message'][0] = contactMessage.value;
  }


  /**
  * Listen for events
  */
  listenEvents() {
    this.contactForm.addEventListener(Events.SUBMIT, (event) => {
      event.preventDefault();

      if (this.isValidData) {
        this.bookAppServices.postContactMessage(this.stateForm);
        this.resetForm_();
      }
    });

    Array.from(this.formInputs, (elem) => {
      utils.addListenerMulti(elem, [Events.INPUT, Events.BLUR,
        Events.CLICK, Events.CHANGE],
      (event) => {
        event.preventDefault();
        new Promise((resolve) => {
          this.setFormState();
          resolve();
        }).then(() => {
          this.validateData(event);
        });
      });
    });
  }


  /**
   * Validates if the form inputs data are the correct one
   * @param {event} event
   */
  validateData(event) {
    const nameValue = this.stateForm['name'][0],
      emailValue = this.stateForm['email'][0],
      messagelValue = this.stateForm['message'][0];

    Array.from(this.formInputs, (elem) => {
      if (elem === event.target) {
        const isValidName = isValidWordCharacter(nameValue),
          isValidEmailValue = isValidEmail(emailValue);

        switch (true) {
          case elem.classList.contains(Classname.NAME_CLASS):
            if (event.type === Events.BLUR && !nameValue) {
              this.stateForm['name'][1] = false;
            } else if (event.type === Events.INPUT && nameValue) {
              this.stateForm['name'][1] = isValidName;
            }
            break;
          case elem.classList.contains(Classname.EMAIL_CLASS):
            if (event.type === Events.BLUR && !emailValue) {
              this.stateForm['email'][1] = false;
            } else if (event.type === Events.INPUT && emailValue) {
              this.stateForm['email'][1] = isValidEmailValue;
            }
            break;
          case elem.classList.contains(Classname.MESSAGE_CLASS):
            if (event.type === Events.BLUR && !messagelValue) {
              this.stateForm['message'][1] = false;
            } else {
              this.stateForm['message'][1] = true;
            }
            break;
        }
      }
    });

    this.isValidData_();
    this.submitObserver_();
  }

  /**
  * Checks if the data setted is valid
  * @private
  */
  isValidData_() {
    this.isValidData = Object.values(this.stateForm).every((elem) => elem[1]);
  }

  /**
   * Submit button observer activates/ deactivates
   * if the form data is valid / invalid
   * @private
   */
  submitObserver_() {
    utils.requestAnimationUtil(() => {
      if (this.isValidData) {
        this.element.querySelector(
          Selectors.SUBMIT_BUTTON).removeAttribute(DataAttributes.DISABLED);
      } else {
        this.element.querySelector(
          Selectors.SUBMIT_BUTTON).setAttribute(
          DataAttributes.DISABLED, DataAttributes.DISABLED);
      }
    }, 0);
  }

  /**
  * Initialize
  */
  init() {
    new Promise((resolve) => {
      utils.printTemplate(contactView);
      resolve();
    }).then(() => {
      this.contactForm = this.element.querySelector(Selectors.CONTACT_FORM);
      this.formInputs = this.element.querySelectorAll(Selectors.FIELD_SELECTOR);
      this.listenEvents();
    });
  }
}


/**
 * Data attributes
 */
const DataAttributes = {
  DISABLED: 'disabled'
};


/**
 * Events
 */
const Events = {
  BLUR: 'blur',
  CHANGE: 'change',
  CLICK: 'click',
  INPUT: 'input',
  SUBMIT: 'submit'
};

/**
 * Class names
 */
const Classname = {
  DISABLED: 'disabled',
  EMAIL_CLASS: 'js-contactEmail',
  MESSAGE_CLASS: 'js-contactMessage',
  NAME_CLASS: 'js-contactName'
};

/**
 * Selectors
 */
const Selectors = {
  CONTACT_EMAIL: `.${Classname.EMAIL_CLASS}`,
  CONTACT_FORM: '#contactForm',
  CONTACT_MESSAGE: `.${Classname.MESSAGE_CLASS}`,
  CONTACT_NAME: `.${Classname.NAME_CLASS}`,
  FIELD_SELECTOR: '.js-formInput',
  FORM_CONTAINER: '.js-contactInputContainer',
  MESSAGE_SUCCED: '.js-succedMessage',
  SUBMIT_BUTTON: '.js-submit'
};

