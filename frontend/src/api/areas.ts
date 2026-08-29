import { apiClient } from './client'
import type { AreaInformacion } from './types'

export async function obtenerInformacionArea(slug: string): Promise<AreaInformacion> {
  const { data } = await apiClient.get<AreaInformacion>(`/${slug}`)
  return data
}