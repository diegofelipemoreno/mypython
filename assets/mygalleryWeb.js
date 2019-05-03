/* eslint-disable no-unused-vars */
import {CONSTANTS} from '../../../../utils/constants.js';
import {BaseComponent} from '../../../../components/js/baseComponent.js';
import {TabContentComponent, DataAttributes}
  from '../../../../components/js/tab-content.js';
import {bookAppServices} from '../../../../appServices.js';
import {galleryComponent} from './gallery.js';
import {modalLoading} from '../../../../components/js/modalLoading.js';
import Vanilla from '../../../../lib/vanillalibrary.js';
import GalleryBase from './gallery-base.js';
import * as utils from '../../../../utils/utils.js';
import * as galleryWebView from '../view/galleryWebView.js';

/**
 * gallery Web Component
 */
export class GalleryWebComponent extends BaseComponent {
  /**
   * creates a actions component
   * @param {!element} element dOM element
   */
  constructor(element) {
    super(element);

    /**
    * Service object data
    */
    this.bookAppServices = bookAppServices();

    /**
     * Initialize TabContentComponent.
     * @private
     */
    this.tabComponent = {};

    /**
    * Array utilities Object
    */
    this.arrayUtils = utils.arrayUtils;

    /**
    * Gallery data Object
    */
    this.galleryData = {};

    /**
    * Gallery Component
    */
    this.galleryComponent = galleryComponent();

    /**
    * Gallery mobile Component
    */
    this.galleryMobileView = GalleryBase.buildItemHtml;

    this.isMobile = Vanilla.isMobile;
    this.heightGallery = 0;
    this.modalLoading = modalLoading();
  }

  /**
   * Gets id type web_gallery
   * @return {string}
   */
  _getIdWebGallery() {
    const IDITEM_PARAM = '&id=',
      fullHasID = window.localStorage.hashFullIds || '';
    let currentId = '';

    if (fullHasID) {
      currentId = fullHasID.split(IDITEM_PARAM)[1] || '';
    }

    return currentId;
  }

  /**
   * Gets data type web_gallery
   */
  setCoverImage() {
    let firstImage;

    Object.values(this.galleryData.gallery).forEach((value, index) => {
      if (!index) {
        firstImage = value.imageUrl || CONSTANTS.DEFAULT_IMAGE;
      }
    });

    this.setAttribute(
      this.element.querySelector(Selectors.IMAGE_COVER), 'src', firstImage);
  }

  /**
   * Sets cover on leave animation
   */
  setCoverBackground() {
    const coverBkSelector
      = this.element.querySelector(Selectors.COVER_BACKGROUND);

    if (this.galleryData && this.galleryData.cover) {
      let coverImage =
        Object.values(this.galleryData.cover)[0]['imageUrl'] ||
        CONSTANTS.DEFAULT_IMAGE;

      coverBkSelector.style.background =
       `url(${coverImage}) center 80px repeat-x`;
    }
  }

  /**
   * sets cover on leave animation
   */
  setCoverAnimation() {
    const coverBkSelector
      = this.element.querySelector(Selectors.COVER_BACKGROUND),
      coverImgSelector = this.element.querySelector(Selectors.COVER_IMAGE);

    if (coverBkSelector) {
      if (window.scrollY > 200) {
        coverImgSelector.classList.add(Classname.COVER_IMAGE_ACTIVE);
        coverBkSelector.classList.add(Classname.COVER_BACKGROUND_ACTIVE);
      } else {
        coverImgSelector.classList.remove(Classname.COVER_IMAGE_ACTIVE);
        coverBkSelector.classList.remove(Classname.COVER_BACKGROUND_ACTIVE);
      }
    }
  }

  /**
   * Sets imac side animation
   */
  setImacSide() {
    let contenImgSelector
      = this.element.querySelector(Selectors.CONTENT_IMAC),
      selectorCoverBk = this.element.querySelector(Selectors.COVER_BACKGROUND);

    selectorCoverBk &&
    utils.observerElement(Selectors.COVER_BACKGROUND, .3, false, () => {
      contenImgSelector.classList.add(Classname.CONTENT_IMAC_ACTIVE);
      utils.requestAnimationUtil(
        () => this.setContentImacSide(), Variables.CONTENT_IMAC_TIME);
    });
  }

  /**
   * Sets main content.
   */
  setMainContent() {
    const mainContentSelector =
      this.element.querySelector(Selectors.MAIN_CONTENT),
      titleSelector =
        mainContentSelector.querySelector(Selectors.CONTENT_MAIN_TITLE),
      textSelector =
        mainContentSelector.querySelector(Selectors.CONTENT_MAIN_TEXT),
      mainTitle = this.galleryData.label,
      mainContent = this.galleryData.info;

    titleSelector.innerHTML = mainTitle;
    textSelector.innerHTML = mainContent;
  }

  /**
   * Sets content on imac side
   */
  setContentImacSide() {
    let imageContentSelector =
      this.element.querySelector(Selectors.CONTENT_SCREEN),
      imageContent,
      itemCoverContentKey,
      currentItemTab;

    if (!imageContentSelector) {
      return;
    }

    this.galleryData.gallery &&
    Object.values(this.galleryData.gallery).forEach((value, index) => {
      if (index &&
        Math.round(window.scrollY / Variables.SCROLL_VALUE) === index) {
        index --;
        imageContent =
          value.imageUrl_640 || value.imageUrl || CONSTANTS.DEFAULT_IMAGE;
        this.setAttribute(imageContentSelector, 'src', imageContent);
        this.setAttribute(imageContentSelector.parentElement,
          DataAttributes.CONTENT_KEY,
          `${DataContentAttr.PREFIX_CONTENT_KEY}${index}`);
      }
    });

    if (imageContentSelector) {
      itemCoverContentKey =
        this.getAttribute(imageContentSelector.parentElement,
          DataAttributes.CONTENT_KEY);
      currentItemTab =
        this.element.querySelector(
          `[${DataAttributes.KEY}='${itemCoverContentKey}']`);
      imageContentSelector.classList.add(Classname.CONTENT_SCREEN_ACTIVE);
      this.tabComponent.setCurrent(currentItemTab);
      this.showTabContent_();
    }
  }

  /**
   * Sets container height
   */
  setContainerHeight() {
    const gallerySize = Object.keys(this.galleryData.gallery).length || 0,
      mainContainer = this.element.querySelector(Selectors.MAIN_CONTAINER);

    this.heightGallery = (gallerySize + 2) * Variables.SCROLL_VALUE;
    mainContainer.style.height = `${this.heightGallery}px`;
  }

  /**
   * Triggers when click tab.
   * @param {Event} event
   * @private
   */
  onClickTab_(event) {
    this.showTabContent_();
  }

  /**
   * Show tab content
   * @private
   */
  showTabContent_() {
    const current = this.tabComponent.getCurrent(),
      coverContentImg = this.element.querySelector(Selectors.CONTENT_SCREEN),
      lastItem =
        this.tabComponent.tabItems_[this.tabComponent.tabItems_.length - 1],
      tabContainer = this.element.querySelector(Selectors.TAB_ITEM_CONTAINER);
    let currentElm = current.el || lastItem,
      currentContentKey = currentElm.getAttribute(DataAttributes.KEY),
      currentImg = currentElm.querySelector(Selectors.TAB_ITEM_IMG_SELECTOR),
      currentSrc = this.getAttribute(currentImg, 'src');

    Array.from(tabContainer.querySelectorAll(
      `[${DataAttributes.CONTENT_KEY}]`), (elem) => {
      elem.classList.remove(Classname.CONTENT_TEXT_VISIBLE);
    });

    tabContainer.querySelector(
      `[${DataAttributes.CONTENT_KEY}='${currentContentKey}']`).classList.add(
      Classname.CONTENT_TEXT_VISIBLE);

    this.setAttribute(coverContentImg, 'src', currentSrc);
    this.tabComponent.checkSelected_();
  }

  /**
   * Init tab component
   * @return {object}  lorem Ipsum is simply dummy   text of the  printing  and
   *   typesetting   industry
   * @private
   */
  initTabComponent_() {
    return new TabContentComponent(
      this.element.querySelector(Selectors.TAB_COMPONENT_SELECTOR),
      A11yValues.ARIA_LABEL_TAB_NAME
    ).init();
  }

  /**
   * Gets data type web_gallery
   */
  render() {
    this.element.innerHTML = '';

    if (this.galleryData.type) {
      if (this.isMobile) {
        this.galleryMobileView(this.galleryData);

        return;
      }

      this.modalLoading.open();
      this.element.classList.remove(Classname.DISABLED);
      utils.requestAnimationUtil(() => {
        utils.printTemplate(galleryWebView);
        this.lazyLoadContent();
        this.setCoverImage();
        this.setCoverBackground();
        this.setContainerHeight();
        this.setListCarrousel();
        this.setMainContent();
        this.tabComponent = this.initTabComponent_();
        utils.imageLazyLoad(Selectors.IMAGE_LAZY_LOAD);
      }, 0);

      utils.requestAnimationUtil(() => {
        utils.observerElement(Selectors.BACKGROUND_COVER, .8, true, () => {
          this.modalLoading.close();
        });

        utils.observerElement(Selectors.CONTACT_FORM, .8, true, () => {
          this.modalLoading.close();
        });
      }, 300);

      utils.requestAnimationUtil(() => {
        this.modalLoading.close();
      }, 500);
    }
  }

  /**
  * Listen for events
  */
  listenEvents() {
    window.addEventListener(Events.SCROLL, () => {
      this.setCoverAnimation();
      this.setImacSide();
    });

    this.element.addEventListener(Events.CLICK, (event) => {
      this.onClickTab_(event);
    });

    window.addEventListener(Events.HASH_CHANGE, () => {
      this.renderTypeWebGallery_();
    });

    this.renderTypeWebGallery_();
  }


  /**
  * Check if hash is for Gallery web
  * @private
  */
  renderTypeWebGallery_() {
    utils.requestAnimationUtil(() => {
      const currentId = this._getIdWebGallery(),
        galleryData = this.bookAppServices.getCurrentItem(currentId);

      new Promise((resolve) => {
        galleryData.on('value', (snapshot) => {
          let subItemObj;

          subItemObj = snapshot.val();

          if (!subItemObj) {
            return;
          }

          this.galleryData = subItemObj;
          resolve(subItemObj);
        });
      }).then((subItemObj) => {
        this.galleryData = subItemObj;
        this.render();
      });
    }, 100);
  }

  /**
  * List Carrousel
  */
  setListCarrousel() {
    const tabContentContainer =
      this.element.querySelector(Selectors.TAB_ITEM_CONTAINER);
    let listContainer,
      imageList,
      listSelector = '',
      textContainer = '';

    Object.values(this.galleryData.gallery).forEach((value, index) => {
      if (index) {
        index --;
        imageList =
          value.imageUrl_640 || value.imageUrl || CONSTANTS.DEFAULT_IMAGE;

        listSelector +=
          `<a href="#" class="${Classname.TAB_ITEM_CLASS}
                              ${Classname.TAB_BUTTON_CLASS}"
            ${DataAttributes.KEY}=
            "${DataContentAttr.PREFIX_CONTENT_KEY}${index}">
              <img class="${Classname.TAB_ITEM_IMG_CLASS}"
                   src="${imageList}" alt="" />
          </a>`;

        textContainer +=
          `<div class="${Classname.CONTENT_TEXT}"
            ${DataAttributes.CONTENT_KEY}=
            ${DataContentAttr.PREFIX_CONTENT_KEY}${index}>
              <p>${value.infoImage}</p>
          </div>`;
      }
    });

    listContainer =
      `<div class="${Classname.TAB_BUTTON_CONTAINER}" role="tablist"
        aria-label="${A11yValues.ARIA_LABEL_TAB_NAME}">
          ${listSelector}
      </div>
      ${textContainer}`;

    tabContentContainer.innerHTML += listContainer;
  }

  /**
   * Hides component until scroll y = 0
   */
  lazyLoadContent() {
    const intervalId = window.setInterval(() => {
      const mainContainer =
        this.element.querySelector(Selectors.MAIN_CONTAINER);

      if (!window.scrollY && mainContainer) {
        window.clearInterval(intervalId);
      }
    }, 300);
  }

  /**
   * initialize component
   */
  init() {
    let flag = false;

    if (this._getIdWebGallery()) {
      this.listenEvents();
    } else {
      const intervalId = window.setInterval(() => {
        if (this._getIdWebGallery() && !flag) {
          flag = true;
          this.listenEvents();
          window.clearInterval(intervalId);
        }
      }, 300);
    }
  }
}


/**
 * Events
 */
const Events = {
  CLICK: 'click',
  HASH_CHANGE: 'hashchange',
  SCROLL: 'scroll'
};


/**
 * A11Y Tab Values
 */
const A11yValues = {
  ARIA_LABEL_TAB_NAME: 'Gallery web project'
};


/**
 * Selectors
 */
const Selectors = {
  BACKGROUND_COVER: '.js-gal-web__background',
  CONTACT_FORM: '.js-contactContainer',
  CONTENT_IMAC: '.gal-web__content-imac',
  CONTENT_SCREEN: '.gal-web__content-screen-img',
  COVER_BACKGROUND: '.gal-web__background',
  CONTENT_MAIN_TITLE: '.gal-web__main-content--title',
  CONTENT_MAIN_TEXT: '.gal-web__main-content--text',
  COVER_IMAGE: '.gal-web__cover-image',
  HEADER_CONTAINER: '.js-headerContainer',
  IMAGE_LAZY_LOAD: '[data-imggalleryweb]',
  IMAGE_COVER: '.gal-web__img-cover',
  MAIN_CONTAINER: '.gal-web__container',
  MAIN_CONTENT: '.gal-web__main-content',
  MENU_CONTAINER: '.js-menuListContainer',
  TAB_BUTTON: '.gal-web__tab-link',
  TAB_COMPONENT_SELECTOR: '[data-tab-component]',
  TAB_ITEM_CONTAINER: '.gal-web__tab',
  TAB_ITEM_TEMPLATE: '.gal-web__tab-list-template',
  TAB_ITEM_SELECTOR: '.gal-web__tab-list',
  TAB_ITEM_IMG_SELECTOR: '.gal-web__tab-img',
  GALLERY_WEB_COMPONENT: '[data-gallerywebview]'
};


/**
 * Class names
 */
const Classname = {
  CONTENT_IMAC_ACTIVE: 'gal-web__content-imac--active',
  CONTENT_SCREEN_ACTIVE: 'gal-web__content-screen-img--active',
  CONTENT_TEXT_VISIBLE: 'gal-web__text--visible',
  CONTENT_TEXT: 'gal-web__text',
  COVER_BACKGROUND_ACTIVE: 'gal-web__background--active',
  COVER_IMAGE_ACTIVE: 'gal-web__cover-image--active',
  DISABLED: 'disabled',
  HEADER_COVER: 'cover--web-gallery',
  MENU_COVER: 'fixedCover',
  MENU_MINIMAL: 'horizontal',
  TAB_BUTTON_CLASS: 'gal-web__tab-link',
  TAB_BUTTON_CONTAINER: 'gal-web__tab-list-container',
  TAB_ITEM_CLASS: 'gal-web__tab-list',
  TAB_ITEM_IMG_CLASS: 'gal-web__tab-img'
};


/**
 * Variables
 */
const Variables = {
  SCROLL_VALUE: 400,
  CONTENT_IMAC_TIME: 280
};


/**
 * Data content Attributes
 * @enum {string} Data content Attributes and more
 */
export const DataContentAttr = {
  PREFIX_CONTENT_KEY: 'actions-content-'
};

/**
 * Data content Attributes
 * @param {String}
 */
export const DataContentAttr = {
  PREFIX_CONTENT_KEY: 'actions-content-'
};

/**
 *  sata content   attributes
 * @enum {Boolean} this is  a text
 */
export const DataContentAttr = {
  PREFIX_CONTENT_KEY: 'actions-content-'
};

/**
 * Data content Attributes
 * @param {!String=}
 */
export const DataContentAttr = {
  PREFIX_CONTENT_KEY: 'actions-content-'
};

/**
 * Data content Attributes
 * @param {Boolean=}
 */
export const DataContentAttr = {
  PREFIX_CONTENT_KEY: 'actions-content-'
};