<script setup lang="ts">
import { useLogtoClient, useLogtoUser, useState, callOnce } from '#imports'

const route = useRoute()
const router = useRouter()
const appConfig = useAppConfig()
const { isHelpSlideoverOpen } = useDashboard()

let isAuth
// adding Logoto Auth
const client = useLogtoClient()
const accessToken = useState<string | undefined>('access-token')

await callOnce(async () => {
  if (!client) {
    throw new Error('Logto client is not available')
  }

  if (!(await client.isAuthenticated())) {
    // TODO: Need to send for Login Page
    console.log('Not Authenticated')
    router.push('/auths/login')
    return
  }

  isAuth = true
  try {
    accessToken.value = await client.getAccessToken()
  } catch (error) {
    console.error('Failed to get access token', error)
  }
})

const user = useLogtoUser()
if (user) {
  console.log(user)
  isAuth = true
}
// ending Logoto Auth

const unsecrureLinks = [{
  id: 'login',
  label: 'Login',
  icon: 'i-heroicons-user',
  to: 'http://localhost:3000/login',
  tooltip: {
    text: 'Login',
    shortcuts: ['G', 'L']
  }
}]

const links = [{
  id: 'home',
  label: 'Home',
  icon: 'i-heroicons-home',
  to: '/',
  tooltip: {
    text: 'Home',
    shortcuts: ['G', 'H']
  }
}, {
  id: 'inbox',
  label: 'Inbox',
  icon: 'i-heroicons-inbox',
  to: '/inbox',
  badge: '4',
  tooltip: {
    text: 'Inbox',
    shortcuts: ['G', 'I']
  }
}, {
  id: 'clients',
  label: 'Clients',
  icon: 'i-heroicons-user',
  to: '/clients',
  tooltip: {
    text: 'Clients',
    shortcuts: ['G', 'C']
  }

},
{
  id: 'invoices',
  label: 'Invoices',
  icon: 'i-heroicons-user',
  to: '/invoices',
  tooltip: {
    text: 'Inv',
    shortcuts: ['G', 'I']
  }

}, {
  id: 'users',
  label: 'Users',
  icon: 'i-heroicons-user-group',
  to: '/users',
  tooltip: {
    text: 'Users',
    shortcuts: ['G', 'U']
  }
}, {
  id: 'settings',
  label: 'Settings',
  to: '/settings',
  icon: 'i-heroicons-cog-8-tooth',
  children: [{
    label: 'General',
    to: '/settings',
    exact: true
  }, {
    label: 'Members',
    to: '/settings/members'
  }, {
    label: 'Notifications',
    to: '/settings/notifications'
  }],
  tooltip: {
    text: 'Settings',
    shortcuts: ['G', 'S']
  }
}]
const menulinks = isAuth ? links : unsecrureLinks
const footerLinks = [{
  label: 'Invite people',
  icon: 'i-heroicons-plus',
  to: '/settings/members'
}, {
  label: 'Help & Support',
  icon: 'i-heroicons-question-mark-circle',
  click: () => isHelpSlideoverOpen.value = true
}]

const groups = [{
  key: 'links',
  label: 'Go to',
  commands: links.map(link => ({ ...link, shortcuts: link.tooltip?.shortcuts }))
}, {
  key: 'code',
  label: 'Code',
  commands: [{
    id: 'source',
    label: 'View page source',
    icon: 'i-simple-icons-github',
    click: () => {
      window.open(`https://github.com/nuxt-ui-pro/dashboard/blob/main/pages${route.path === '/' ? '/index' : route.path}.vue`, '_blank')
    }
  }]
}]

const defaultColors = ref(['green', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet'].map(color => ({ label: color, chip: color, click: () => appConfig.ui.primary = color })))
const colors = computed(() => defaultColors.value.map(color => ({ ...color, active: appConfig.ui.primary === color.label })))
</script>

<template>
  <UDashboardLayout>
    <UDashboardPanel
      :width="250"
      :resizable="{ min: 200, max: 300 }"
      collapsible
    >
      <UDashboardNavbar
        class="!border-transparent"
        :ui="{ left: 'flex-1' }"
      >
        <template #left>
          <TeamsDropdown :is-auth="isAuth" />
        </template>
      </UDashboardNavbar>

      <UDashboardSidebar>
        <template #header>
          <UDashboardSearchButton />
        </template>

        <UDashboardSidebarLinks :links="menulinks" />

        <UDivider />

        <UDashboardSidebarLinks
          v-if="isAuth"
          :links="[{ label: 'Colors', draggable: true, children: colors }]"
          @update:links="colors => defaultColors = colors"
        />

        <div class="flex-1" />

        <UDashboardSidebarLinks
          v-if="isAuth"
          :links="footerLinks"
        />

        <UDivider class="sticky bottom-0" />

        <template
          v-if="isAuth"
          #footer
        >
          <!-- ~/components/UserDropdown.vue -->
          <UserDropdown />
        </template>
      </UDashboardSidebar>
    </UDashboardPanel>

    <slot v-if="isAuth" />

    <!-- ~/components/HelpSlideover.vue -->
    <HelpSlideover />
    <!-- ~/components/NotificationsSlideover.vue -->
    <NotificationsSlideover />

    <ClientOnly v-if="isAuth">
      <LazyUDashboardSearch :groups="groups" />
    </ClientOnly>
  </UDashboardLayout>
</template>
