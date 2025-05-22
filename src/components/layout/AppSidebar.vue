<!--
  Componente AppSidebar
  Barra lateral de navegación principal.
  Incluye logo, menú de navegación y submenús.
-->
<template>
  <aside
    :class="[
      'fixed mt-16 flex flex-col lg:mt-0 top-0 px-5 left-0 bg-white dark:bg-gray-900 dark:border-gray-800 text-gray-900 h-screen transition-all duration-500 ease-in-out z-99999 border-r border-gray-200',
      {
        'lg:w-[290px]': isExpanded || isMobileOpen || isHovered,
        'lg:w-[90px]': !isExpanded && !isHovered,
        'translate-x-0 w-[290px]': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
        'lg:translate-x-0': true,
      },
    ]"
    @mouseenter="!isExpanded && (isHovered = true)"
    @mouseleave="isHovered = false"
  >
    <div
      :class="[
        'py-8 flex',
        !isExpanded && !isHovered ? 'lg:justify-center' : 'justify-start',
      ]"
    >
      <router-link to="/">
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          class="dark:hidden"
          src="/images/logo/banner_huam.png"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          class="hidden dark:block"
          src="/images/logo/logo-dark.svg"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-else
          src="/images/logo/icon-huam.webp"
          alt="Logo"
          width="32"
          height="32"
        />
      </router-link>
    </div>
    <div
      class="flex flex-col overflow-y-auto duration-500 ease-in-out no-scrollbar"
    >
      <nav class="mb-6">
        <div class="flex flex-col gap-4">
          <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
            <h2
              :class="[
                'mb-4 text-xs uppercase flex leading-[20px] text-gray-400',
                !isExpanded && !isHovered
                  ? 'lg:justify-center'
                  : 'justify-start',
              ]"
            >
              <template v-if="isExpanded || isHovered || isMobileOpen">
                {{ menuGroup.title }}
              </template>
              <HorizontalDots v-else />
            </h2>
            <ul class="flex flex-col gap-4">
              <li v-for="(item, index) in menuGroup.items" :key="item.name">
                <button
                  v-if="item.subItems"
                  @click="toggleSubmenu(groupIndex, index)"
                  :class="[
                    'menu-item group w-full transition-all duration-300 ease-in-out',
                    {
                      'menu-item-active': isSubmenuOpen(groupIndex, index),
                      'menu-item-inactive': !isSubmenuOpen(groupIndex, index),
                    },
                    !isExpanded && !isHovered
                      ? 'lg:justify-center'
                      : 'lg:justify-start',
                  ]"
                >
                  <span
                    :class="[
                      'transition-colors duration-300 ease-in-out',
                      isSubmenuOpen(groupIndex, index)
                        ? 'menu-item-icon-active'
                        : 'menu-item-icon-inactive',
                    ]"
                  >
                    <component :is="item.icon" />
                  </span>
                  <span
                    v-if="isExpanded || isHovered || isMobileOpen"
                    class="menu-item-text transition-opacity duration-300 ease-in-out"
                    >{{ item.name }}</span
                  >
                  <ChevronDownIcon
                    v-if="isExpanded || isHovered || isMobileOpen"
                    :class="[
                      'ml-auto w-5 h-5 transition-transform duration-300 ease-in-out',
                      {
                        'rotate-180 text-brand-500': isSubmenuOpen(
                          groupIndex,
                          index
                        ),
                      },
                    ]"
                  />
                </button>
                <router-link
                  v-else-if="item.path"
                  :to="item.path"
                  :class="[
                    'menu-item group transition-all duration-300 ease-in-out',
                    {
                      'menu-item-active': isActive(item.path),
                      'menu-item-inactive': !isActive(item.path),
                    },
                  ]"
                >
                  <span
                    :class="[
                      'transition-colors duration-300 ease-in-out',
                      isActive(item.path)
                        ? 'menu-item-icon-active'
                        : 'menu-item-icon-inactive',
                    ]"
                  >
                    <component :is="item.icon" />
                  </span>
                  <span
                    v-if="isExpanded || isHovered || isMobileOpen"
                    class="menu-item-text transition-opacity duration-300 ease-in-out"
                    >{{ item.name }}</span
                  >
                </router-link>
                <div
                  v-show="
                    isSubmenuOpen(groupIndex, index) &&
                    (isExpanded || isHovered || isMobileOpen)
                  "
                >
                  <ul class="mt-2 space-y-1 ml-9">
                    <li v-for="subItem in item.subItems" :key="subItem.name">
                      <router-link
                        :to="subItem.path"
                        :class="[
                          'menu-dropdown-item transition-all duration-300 ease-in-out',
                          {
                            'menu-dropdown-item-active': isActive(
                              subItem.path
                            ),
                            'menu-dropdown-item-inactive': !isActive(
                              subItem.path
                            ),
                          },
                        ]"
                      >
                        {{ subItem.name }}
                        <span class="flex items-center gap-1 ml-auto">
                          <span
                            v-if="subItem.new"
                            :class="[
                              'menu-dropdown-badge transition-colors duration-300 ease-in-out',
                              {
                                'menu-dropdown-badge-active': isActive(
                                  subItem.path
                                ),
                                'menu-dropdown-badge-inactive': !isActive(
                                  subItem.path
                                ),
                              },
                            ]"
                          >
                            new
                          </span>
                          <span
                            v-if="subItem.pro"
                            :class="[
                              'menu-dropdown-badge transition-colors duration-300 ease-in-out',
                              {
                                'menu-dropdown-badge-active': isActive(
                                  subItem.path
                                ),
                                'menu-dropdown-badge-inactive': !isActive(
                                  subItem.path
                                ),
                              },
                            ]"
                          >
                            pro
                          </span>
                        </span>
                      </router-link>
                    </li>
                  </ul>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed, type Component } from "vue";
import { useRoute } from "vue-router";

import {
  GridIcon,
  CalenderIcon,
  UserCircleIcon,
  PieChartIcon,
  ChevronDownIcon,
  HorizontalDots,
  PageIcon,
  TableIcon,
  ListIcon,
  PlugInIcon,
} from "../../icons";
import BoxCubeIcon from "@/icons/BoxCubeIcon.vue";
import { useSidebar } from "@/composables/useSidebar";

const route = useRoute();

const { isExpanded, isMobileOpen, isHovered, openSubmenu } = useSidebar();

interface SubMenuItem {
  name: string;
  path: string;
  pro: boolean;
  new?: boolean;
}

interface MenuItem {
  icon: Component;
  name: string;
  path?: string;
  pro?: boolean;
  subItems?: SubMenuItem[];
}

interface MenuGroup {
  title: string;
  items: MenuItem[];
}

const menuGroups: MenuGroup[] = [
  {
    title: "Menu",
    items: [
      {
        icon: GridIcon,
        name: "Inicio",
        path: "/",
        pro: false
      },
      {
        name: "Agregar muestra",
        icon: ListIcon,
        subItems: [
          { name: "Nueva muestra", path: "/nueva-muestra", pro: false },
          { name: "Editar muestra", path: "/editar-muestra", pro: false },
        ],
      },
      {
        name: "Listado de muestras",
        icon: TableIcon,
        subItems: [
          { name: "Muestras actuales", path: "/listado-muestras-actuales", pro: false },
          { name: "Muestras anteriores", path: "/listado-muestras-anteriores", pro: false }
        ],
      },
      {
        name: "Informes",
        icon: PageIcon,
        subItems: [
          { name: "Realizar informe", path: "/realizar-informe", pro: false },
          { name: "Validar informe", path: "/validar-informe", pro: false },
          { name: "Listado de informes", path: "/listado-informes", pro: false },
        ],
      },
      {
        icon: PieChartIcon,
        name: "Estadisticas",
        subItems: [
          { name: "Line Chart", path: "/line-chart", pro: false },
          { name: "Bar Chart", path: "/bar-chart", pro: false },
        ],
      },
      {
        icon: CalenderIcon,
        name: "Calendar",
        path: "/calendar",
      },
    ],
  },
  {
    title: "Others",
    items: [
      {
        icon: UserCircleIcon,
        name: "User Profile",
        path: "/profile",
      },
      {
        icon: PlugInIcon,
        name: "Authentication",
        subItems: [
          { name: "Inicio de sesión", path: "/inicio-sesion", pro: false },
        ],
      },
      {
        icon: BoxCubeIcon,
        name: "Ui Elements",
        subItems: [
          { name: "Alerts", path: "/alerts", pro: false },
          { name: "Avatars", path: "/avatars", pro: false },
          { name: "Badge", path: "/badge", pro: false },
          { name: "Buttons", path: "/buttons", pro: false },
          { name: "Images", path: "/images", pro: false },
          { name: "Videos", path: "/videos", pro: false },
        ],
      },
    ],
  },
];

const isActive = (path: string): boolean => route.path === path;

const toggleSubmenu = (groupIndex: number, itemIndex: number): void => {
  const key = `${groupIndex}-${itemIndex}`;
  openSubmenu.value = openSubmenu.value === key ? null : key;
};

const isAnySubmenuRouteActive = computed(() => {
  return menuGroups.some((group) =>
    group.items.some(
      (item) =>
        item.subItems && item.subItems.some((subItem) => isActive(subItem.path))
    )
  );
});

const isSubmenuOpen = (groupIndex: number, itemIndex: number): boolean => {
  const key = `${groupIndex}-${itemIndex}`;
  const item = menuGroups[groupIndex]?.items[itemIndex];
  return (
    openSubmenu.value === key ||
    (isAnySubmenuRouteActive.value && (item?.subItems?.some((subItem) => isActive(subItem.path)) ?? false))
  );
};
</script>

<style scoped>
/* Animación de deslizamiento y desvanecimiento para submenús */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}

/* Mejora del scroll */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Estilos de transición para elementos del menú */
.menu-item,
.menu-dropdown-item {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-item:hover,
.menu-dropdown-item:hover {
  background-color: rgba(59, 130, 246, 0.1);
  transform: translateX(4px);
}

/* Transiciones para íconos y badges */
.menu-item-icon-active,
.menu-item-icon-inactive,
.menu-dropdown-badge {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
