// store.ts
import { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore,Store } from 'vuex'

// ストアのステートに対して型を定義します
export interface State {
  count: number
}

// インジェクションキーを定義します
export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
  state: {
    count: 1
  }
})

export function useStore () {
  return baseUseStore(key)
}